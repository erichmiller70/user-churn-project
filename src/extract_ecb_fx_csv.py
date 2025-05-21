# src/extract_ecb_fx_csv.py
import pandas as pd, requests, io
from extract_base import save_df

URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.csv"

def main():
    csv = requests.get(URL, timeout=30).text
    df = pd.read_csv(io.StringIO(csv))
    save_df(df, "ecb", "fx_rates")

if __name__ == "__main__":
    main()
