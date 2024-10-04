# app/utils.py
import math

import httpx
from .config import settings
from .models import ProfitabilityOutput

async def get_bitcoin_price():
    """
    Fetch the current Bitcoin price in USD from CoinGecko API.
    """
    url = f"{settings.COIN_GECKO_API_URL}/simple/price"
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data['bitcoin']['usd']

async def get_network_difficulty():
    """
    Fetch the current Bitcoin network difficulty.
    Using CoinGecko API as an example; adjust based on available endpoints.
    """
    # Note: CoinGecko may not provide network difficulty.
    # You might need to use another API like Blockchain.info or similar.
    # For demonstration, we'll use a placeholder value.
    return 25_000_000_000  # Placeholder value

def calculate_profitability(electricity_cost, hash_rate, initial_investment, power_consumption, btc_price_usd, network_difficulty) -> ProfitabilityOutput:
    """Calculate the profitability of Bitcoin mining."""
    block_reward_btc = 6.25  # Current Bitcoin block reward
    seconds_per_day = 86400  # 24 hours * 60 minutes * 60 seconds

    # Calculate daily BTC revenue based on hash rate and network difficulty
    btc_per_day = (hash_rate * 1e12 / network_difficulty) * block_reward_btc * (seconds_per_day / 600)

    # Calculate daily revenue in USD
    daily_revenue_usd = btc_per_day * btc_price_usd
    monthly_revenue_usd = daily_revenue_usd * 30
    yearly_revenue_usd = daily_revenue_usd * 365

    # Calculate electricity costs
    daily_cost_usd = (power_consumption / 1000) * 24 * electricity_cost
    monthly_cost_usd = daily_cost_usd * 30
    yearly_cost_usd = daily_cost_usd * 365

    # Calculate profit
    daily_profit_usd = daily_revenue_usd - daily_cost_usd
    monthly_profit_usd = daily_profit_usd * 30
    yearly_profit_usd = daily_profit_usd * 365

    # Calculate breakeven timeline (in months)
    if daily_profit_usd > 0:
        breakeven_timeline_months = initial_investment / monthly_profit_usd
    else:
        breakeven_timeline_months = math.inf  # If no profit, breakeven is never reached

    # Calculate cost to mine 1 BTC
    if btc_per_day > 0:
        cost_to_mine_one_btc = daily_cost_usd / btc_per_day
    else:
        cost_to_mine_one_btc = math.inf  # If BTC mined is 0, cost is infinite

    # Create and return a ProfitabilityOutput instance
    return ProfitabilityOutput(
        dailyCost=daily_cost_usd,
        monthlyCost=monthly_cost_usd,
        yearlyCost=yearly_cost_usd,
        dailyRevenueUSD=daily_revenue_usd,
        monthlyRevenueUSD=monthly_revenue_usd,
        yearlyRevenueUSD=yearly_revenue_usd,
        dailyRevenueBTC=btc_per_day,
        monthlyRevenueBTC=btc_per_day * 30,
        yearlyRevenueBTC=btc_per_day * 365,
        dailyProfitUSD=daily_profit_usd,
        monthlyProfitUSD=monthly_profit_usd,
        yearlyProfitUSD=yearly_profit_usd,
        breakevenTimeline=breakeven_timeline_months,
        costToMine=cost_to_mine_one_btc
    )