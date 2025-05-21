# src/extract_nyc311_api.py
import requests, pandas as pd
from extract_base import save_df
from datetime import datetime, timedelta

# last 30 days of tickets; Socrata caps at 50 k rows per call
since = (datetime.utcnow() - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%S")
URL = ("https://data.cityofnewyork.us/resource/erm2-nwe9.json"
       f"?$where=created_date>='{since}'&$limit=50000")

def main():
    data = requests.get(URL, timeout=60).json()
    df = pd.DataFrame(data)
    save_df(df, "api", "nyc_311_tickets")

if __name__ == "__main__":
    main()
