# fetch_alpha_vantage_data.py
import requests
import pandas as pd
from datetime import datetime

def fetch_alpha_vantage_data(symbol, api_key, interval='5min'):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "apikey": api_key,
        "outputsize": "compact",
    }
    response = requests.get(url, params=params)
    data = response.json()
    time_series_key = f"Time Series ({interval})"
    if time_series_key in data:
        df = pd.DataFrame.from_dict(data[time_series_key], orient="index")
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        return df
    else:
        print("Error fetching Alpha Vantage data:", data)
        return None

if __name__ == "__main__":
    ALPHA_VANTAGE_API_KEY = "your-alpha-vantage-api-key"
    SYMBOL = "IBM"
    df = fetch_alpha_vantage_data(SYMBOL, ALPHA_VANTAGE_API_KEY)
    if df is not None:
        df.to_parquet(f"alpha_vantage_{SYMBOL}_{datetime.now().strftime('%Y-%m-%d')}.parquet")
        print("Alpha Vantage data saved locally.")