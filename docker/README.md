ECH-AI V1
This is a proof of concept for an AI-powered hedge fund. The goal of this project is to explore the use of AI to make trading decisions. This project is for educational purposes only and is not intended for real trading or investment.

This system employs several agents working together:

Aswath Damodaran Agent - The Dean of Valuation, focuses on story, numbers, and disciplined valuation
Ben Graham Agent - The godfather of value investing, only buys hidden gems with a margin of safety
Bill Ackman Agent - An activist investor, takes bold positions and pushes for change
Cathie Wood Agent - The queen of growth investing, believes in the power of innovation and disruption
Charlie Munger Agent - Warren Buffett's partner, only buys wonderful businesses at fair prices
Michael Burry Agent - The Big Short contrarian who hunts for deep value
Mohnish Pabrai Agent - The Dhandho investor, who looks for doubles at low risk
Peter Lynch Agent - Practical investor who seeks "ten-baggers" in everyday businesses
Phil Fisher Agent - Meticulous growth investor who uses deep "scuttlebutt" research
Rakesh Jhunjhunwala Agent - The Big Bull of India
Stanley Druckenmiller Agent - Macro legend who hunts for asymmetric opportunities with growth potential
Warren Buffett Agent - The oracle of Omaha, seeks wonderful companies at a fair price
Valuation Agent - Calculates the intrinsic value of a stock and generates trading signals
Sentiment Agent - Analyzes market sentiment and generates trading signals
Fundamentals Agent - Analyzes fundamental data and generates trading signals
Technicals Agent - Analyzes technical indicators and generates trading signals
Risk Manager - Calculates risk metrics and sets position limits
Portfolio Manager - Makes final trading decisions and generates orders
Screenshot 2025-03-22 at 6 19 07 PM
Note: the system does not actually make any trades.

Twitter Follow

Disclaimer
This project is for educational and research purposes only.

Not intended for real trading or investment
No investment advice or guarantees provided
Creator assumes no liability for financial losses
Consult a financial advisor for investment decisions
Past performance does not indicate future results
By using this software, you agree to use it solely for learning purposes.

Table of Contents
How to Install
How to Run
⌨️ Command Line Interface
🖥️ Web Application (NEW!)
Contributing
Feature Requests
License
How to Install
Before you can run the AI Hedge Fund, you'll need to install it and set up your API keys. These steps are common to both the full-stack web application and command line interface.

1. Clone the Repository
git clone https://github.com/virattt/ai-hedge-fund.git
cd ai-hedge-fund
2. Set Up Your API Keys
Create a .env file for your API keys:

# Create .env file for your API keys (in the root directory)
cp .env.example .env
Open and edit the .env file to add your API keys:

# For running LLMs hosted by openai (gpt-4o, gpt-4o-mini, etc.)
OPENAI_API_KEY=your-openai-api-key

# For getting financial data to power the hedge fund
FINANCIAL_DATASETS_API_KEY=your-financial-datasets-api-key
Important: You must set at least one LLM API key (e.g. OPENAI_API_KEY, GROQ_API_KEY, ANTHROPIC_API_KEY, or DEEPSEEK_API_KEY) for the hedge fund to work.

Financial Data: Data for AAPL, GOOGL, MSFT, NVDA, and TSLA is free and does not require an API key. For any other ticker, you will need to set the FINANCIAL_DATASETS_API_KEY in the .env file.

How to Run
⌨️ Command Line Interface
For users who prefer working with command line tools, you can run the AI Hedge Fund directly via terminal. This approach offers more granular control and is useful for automation, scripting, and integration purposes.

Screenshot 2025-01-06 at 5 50 17 PM
Using Docker
Make sure you have Docker installed on your system. If not, you can download it from Docker's official website.

Navigate to the docker directory:

cd docker
Build the Docker image:
# On Linux/Mac:
./run.sh build

# On Windows:
run.bat build
Running the AI Hedge Fund (with Docker)
# Navigate to the docker directory first
cd docker

# On Linux/Mac:
./run.sh --ticker AAPL,MSFT,NVDA main

# On Windows:
run.bat --ticker AAPL,MSFT,NVDA main
You can also specify a --ollama flag to run the AI hedge fund using local LLMs.

# With Docker (from docker/ directory):
# On Linux/Mac:
./run.sh --ticker AAPL,MSFT,NVDA --ollama main

# On Windows:
run.bat --ticker AAPL,MSFT,NVDA --ollama main
If you already have an Ollama server running (locally or on your network), point the containers at it instead of starting the bundled instance. You can either pass an explicit base URL or export OLLAMA_BASE_URL before running the scripts.

# Linux / macOS
./run.sh --ticker AAPL,MSFT,NVDA --ollama --ollama-base-url http://localhost:11434 main

# Windows
run.bat --ticker AAPL,MSFT,NVDA --ollama --ollama-base-url http://localhost:11434 main
When OLLAMA_BASE_URL is provided, the Docker compose services reuse that endpoint and the Ollama container is not started. To launch the embedded Ollama service manually with Docker Compose, add the embedded-ollama profile (e.g. docker compose --profile embedded-ollama up).

You can optionally specify the start and end dates to make decisions for a specific time period.

# With Docker (from docker/ directory):
# On Linux/Mac:
./run.sh --ticker AAPL,MSFT,NVDA --start-date 2024-01-01 --end-date 2024-03-01 main

# On Windows:
run.bat --ticker AAPL,MSFT,NVDA --start-date 2024-01-01 --end-date 2024-03-01 main
Running the Backtester (with Docker)
# Navigate to the docker directory first
cd docker

# On Linux/Mac:
./run.sh --ticker AAPL,MSFT,NVDA backtest

# On Windows:
run.bat --ticker AAPL,MSFT,NVDA backtest
Example Output: Screenshot 2025-01-06 at 5 47 52 PM

You can optionally specify the start and end dates to backtest over a specific time period.

# With Docker (from docker/ directory):
# On Linux/Mac:
./run.sh --ticker AAPL,MSFT,NVDA --start-date 2024-01-01 --end-date 2024-03-01 backtest

# On Windows:
run.bat --ticker AAPL,MSFT,NVDA --start-date 2024-01-01 --end-date 2024-03-01 backtest
You can also specify a --ollama flag to run the backtester using local LLMs.

# With Docker (from docker/ directory):
# On Linux/Mac:
./run.sh --ticker AAPL,MSFT,NVDA --ollama backtest

# On Windows:
run.bat --ticker AAPL,MSFT,NVDA --ollama backtest
Contributing
Fork the repository
Create a feature branch
Commit your changes
Push to the branch
Create a Pull Request
Important: Please keep your pull requests small and focused. This will make it easier to review and merge.

