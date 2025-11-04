from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import logging
import asyncio
import os
from pathlib import Path

from app.backend.routes import api_router
from app.backend.database.connection import engine
from app.backend.database.models import Base
from app.backend.services.ollama_service import ollama_service

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="ECH AI API", description="Backend API for ECH AI", version="0.1.0")

# Initialize database tables (this is safe to run multiple times)
Base.metadata.create_all(bind=engine)

# Configure CORS
# Get allowed origins from environment or use defaults for development
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Frontend URLs (dev + production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routes
app.include_router(api_router)

# Serve static frontend files in production
# Path calculation: app/backend/main.py -> app/backend -> app -> frontend/dist
frontend_dist_path = Path(__file__).parent.parent / "frontend" / "dist"
logger.info(f"Looking for frontend at: {frontend_dist_path}")
logger.info(f"Frontend dist exists: {frontend_dist_path.exists()}")
if frontend_dist_path.exists():
    logger.info(f"Frontend assets path: {frontend_dist_path / 'assets'}")
    # Mount static files
    app.mount("/assets", StaticFiles(directory=frontend_dist_path / "assets"), name="assets")
    
    # Serve index.html for all non-API routes (must be after all other routes)
    # FastAPI should match specific routes first, but we'll exclude API routes explicitly
    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        """
        Serve the React frontend for all non-API routes.
        This catch-all must be last to not interfere with API routes.
        Exclude API routes and static assets.
        """
        # Exclude API routes and static assets - FastAPI should have handled these already
        # but we check here as a safety measure
        api_routes = ["hedge-fund", "flows", "api-keys", "ollama", "language-models", "storage", "ping", "docs", "redoc", "openapi.json"]
        if any(full_path.startswith(route + "/") or full_path == route for route in api_routes) or full_path.startswith("assets/"):
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail="API route not found")
        
        index_file = frontend_dist_path / "index.html"
        logger.info(f"Serving frontend for path: {full_path}, index exists: {index_file.exists()}")
        if index_file.exists():
            return FileResponse(index_file)
        return {"detail": "Frontend not found"}
else:
    logger.warning("Frontend dist directory not found! Frontend will not be served.")

@app.on_event("startup")
async def startup_event():
    """Startup event to check Ollama availability."""
    try:
        logger.info("Checking Ollama availability...")
        status = await ollama_service.check_ollama_status()
        
        if status["installed"]:
            if status["running"]:
                logger.info(f"✓ Ollama is installed and running at {status['server_url']}")
                if status["available_models"]:
                    logger.info(f"✓ Available models: {', '.join(status['available_models'])}")
                else:
                    logger.info("ℹ No models are currently downloaded")
            else:
                logger.info("ℹ Ollama is installed but not running")
                logger.info("ℹ You can start it from the Settings page or manually with 'ollama serve'")
        else:
            logger.info("ℹ Ollama is not installed. Install it to use local models.")
            logger.info("ℹ Visit https://ollama.com to download and install Ollama")
            
    except Exception as e:
        logger.warning(f"Could not check Ollama status: {e}")
        logger.info("ℹ Ollama integration is available if you install it later")
