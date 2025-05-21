# src/extract_base.py
"""Utilities shared by all extract scripts."""

import os, pathlib, datetime, pandas as pd, json
from dotenv import load_dotenv

load_dotenv()                       # pulls creds from .env

RAW_DIR = pathlib.Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = pathlib.Path("data/data_log.csv")

def timestamp() -> str:
    return datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")

def save_df(df: pd.DataFrame, source: str, name: str):
    fn = RAW_DIR / f"{source}__{name}__{timestamp()}.parquet"
    df.to_parquet(fn, index=False)
    _log(fn, len(df))
    print(f"Saved {len(df):,} rows ➜ {fn}")
    return fn

def save_json(obj: dict | list, source: str, name: str):
    fn = RAW_DIR / f"{source}__{name}__{timestamp()}.json"
    pathlib.Path(fn).write_text(json.dumps(obj, indent=2))
    _log(fn, len(obj))
    print(f"Saved {len(obj):,} records ➜ {fn}")
    return fn

def _log(path, n_rows: int):
    entry = pd.DataFrame([[str(path), timestamp(), n_rows]],
                         columns=["file", "extracted_at_utc", "rows"])
    header = not LOG_FILE.exists()
    entry.to_csv(LOG_FILE, mode="a", header=header, index=False)
