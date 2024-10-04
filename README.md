# Bitcoin Mining Calculator Backend

This repository contains a **FastAPI** backend for calculating the profitability of Bitcoin mining operations based on user inputs. It interfaces with a provided frontend to deliver real-time profitability estimates.


## Features

- **Profitability Calculation**: The API computes various profitability metrics based on user input, including:
  - Daily, monthly, and yearly costs
  - Daily, monthly, and yearly revenues (in both USD and BTC)
  - Daily, monthly, and yearly profits (in USD)
  - Breakeven timeline
  - Cost to mine 1 BTC

## Assumptions
  - The electricity cost is provided in USD per kWh.
  - Hash rate is provided in TH/s. 
  - Power consumption is provided in Watts.
  - The current Bitcoin block reward is assumed to be 6.25 BTC.

## API Endpoints

### Calculate Profitability

- **Endpoint**: `/calculate/`
- **Method**: `POST`
- **Request Body**: The request must contain the following fields:

```json
{
  "electricity_cost": 0.1,       // Electricity cost in USD per kWh
  "hash_rate": 100,               // Hash rate in TH/s
  "initial_investment": 100,      // Initial investment in USD
  "power_consumption": 3000        // Power consumption in Watts
}
```

- **Response**: The response will return a JSON object with the calculated profitability metrics:

```
{
  "dailyCost": 10.0,
  "monthlyCost": 300.0,
  "yearlyCost": 3600.0,
  "dailyRevenueUSD": 15.0,
  "monthlyRevenueUSD": 450.0,
  "yearlyRevenueUSD": 5400.0,
  "dailyRevenueBTC": 0.0003,
  "monthlyRevenueBTC": 0.009,
  "yearlyRevenueBTC": 0.108,
  "dailyProfitUSD": 5.0,
  "monthlyProfitUSD": 150.0,
  "yearlyProfitUSD": 1800.0,
  "breakevenTimeline": 2.0,
  "costToMine": 33.33
}
```

## Installation
### Prerequisites
Make sure you have Python 3.7 or higher installed.

### Steps to Set Up the Project
#### Clone the Repository:

```bash
git clone https://github.com/hmunjuluri05/bitcoin-mining-calculator-backend.git
cd bitcoin-mining-calculator-backend
```

#### Install Dependencies: 
You can install the required dependencies using pip. It’s recommended to create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

#### Run the Application: 
Start the FastAPI application with the following command:

```bash
uvicorn app.main:app --reload
````
#### Access the API: 
  - The API will be running at http://localhost:8000
  - You can access the interactive API documentation at http://localhost:8000/docs

