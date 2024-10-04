from pydantic import BaseModel

class ProfitabilityInput(BaseModel):
    electricity_cost: float  # Electricity cost in USD per kWh
    hash_rate: float         # Hash rate in TH/s
    initial_investment: float # Initial investment in USD
    power_consumption: float  # Power consumption in Watts