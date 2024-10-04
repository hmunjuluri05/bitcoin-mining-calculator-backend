from pydantic import BaseModel

class ProfitabilityOutput(BaseModel):
    dailyCost: float
    monthlyCost: float
    yearlyCost: float
    dailyRevenueUSD: float
    monthlyRevenueUSD: float
    yearlyRevenueUSD: float
    dailyRevenueBTC: float
    monthlyRevenueBTC: float
    yearlyRevenueBTC: float
    dailyProfitUSD: float
    monthlyProfitUSD: float
    yearlyProfitUSD: float
    breakevenTimeline: float
    costToMine: float
