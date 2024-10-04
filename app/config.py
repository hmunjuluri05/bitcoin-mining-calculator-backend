# app/config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # External APIs
    COIN_GECKO_API_URL: str = "https://api.coingecko.com/api/v3"
    # You can add more API URLs or keys here if needed

settings = Settings()
