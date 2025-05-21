# src/extract_telco_csv.py
import pandas as pd, pathlib, requests, io
from extract_base import save_df

URL = ("https://raw.githubusercontent.com/SohelRaja/Customer-Churn-Analysis/"
       "master/Decision%20Tree/WA_Fn-UseC_-Telco-Customer-Churn.csv")

def main():
    resp = requests.get(URL, timeout=30)
    resp.raise_for_status()
    df = pd.read_csv(io.StringIO(resp.text))
    save_df(df, "github", "telco_customers")

if __name__ == "__main__":
    main()
