from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models.profitability_input import ProfitabilityInput
from .models.profitability_output import ProfitabilityOutput
from .utils import get_bitcoin_price, get_network_difficulty, calculate_profitability

app = FastAPI(
    title="Bitcoin Mining Profitability Calculator API",
    description="API to calculate the profitability of Bitcoin mining operations based on user inputs.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # This allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # This allows all headers
)

@app.post("/calculate/", response_model=ProfitabilityOutput)
async def calculate(data: ProfitabilityInput):
    # Fetching Bitcoin price and network difficulty from utils
    btc_price_usd = await get_bitcoin_price()
    network_difficulty = await get_network_difficulty()

    # Call the profitability calculation function from utils
    result = calculate_profitability(
        electricity_cost=data.electricity_cost,
        hash_rate=data.hash_rate,
        initial_investment=data.initial_investment,
        power_consumption=data.power_consumption,
        btc_price_usd=btc_price_usd,
        network_difficulty=network_difficulty
    )

    return result
