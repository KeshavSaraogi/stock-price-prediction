import requests
import pandas as pd

def fetch_alpha_vantage_data(symbol, api_key, interval='daily'):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key,
        "outputsize": "compact",
    }
    response = requests.get(url, params=params)
    data = response.json()
    time_series_key = "Time Series (Daily)"
    if time_series_key in data:
        df = pd.DataFrame.from_dict(data[time_series_key], orient="index")
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        return df
    else:
        print("Error fetching Alpha Vantage data:", data)
        return None

def fetch_company_overview(symbol, api_key):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "OVERVIEW",
        "symbol": symbol,
        "apikey": api_key,
    }
    response = requests.get(url, params=params)
    data = response.json()
    if "Symbol" in data:
        return pd.DataFrame([data])
    else:
        print("Error fetching company overview:", data)
        return None

def fetch_technical_indicators(symbol, api_key, indicator="SMA", interval="daily"):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": indicator,
        "symbol": symbol,
        "interval": interval,
        "time_period": 20,
        "series_type": "close",
        "apikey": api_key,
    }
    response = requests.get(url, params=params)
    data = response.json()
    key = f"Technical Analysis: {indicator}"
    if key in data:
        df = pd.DataFrame.from_dict(data[key], orient="index")
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        return df
    else:
        print(f"Error fetching {indicator} data:", data)
        return None
