import pandas as pd
from datetime import datetime
from helper import fetch_alpha_vantage_data, fetch_company_overview, fetch_technical_indicators

def process_stock_data(symbol, api_key):
    df_price = fetch_alpha_vantage_data(symbol, api_key)
    df_overview = fetch_company_overview(symbol, api_key)
    df_sma = fetch_technical_indicators(symbol, api_key, "SMA")

    if df_price is not None and df_overview is not None and df_sma is not None:
        df_combined = pd.concat([df_price, df_sma], axis=1)

        price_filename = f"alpha_vantage_{symbol}_{datetime.now().strftime('%Y-%m-%d')}.parquet"
        overview_filename = f"company_overview_{symbol}_{datetime.now().strftime('%Y-%m-%d')}.parquet"

        df_combined.to_parquet(price_filename)
        df_overview.to_parquet(overview_filename)

        print(f"Data processing completed. Files saved: {price_filename}, {overview_filename}")
        return [price_filename, overview_filename]
    else:
        print("Data processing failed due to missing data.")
        return None
