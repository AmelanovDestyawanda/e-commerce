import pandas as pd

def load_data(path="data/ecom.csv"):
    """
    Load data dari CSV dengan auto-detect delimiter
    """
    print("Loading data...")
    
    try:
        df = pd.read_csv(
            path,
            encoding="latin1",
            sep=None,          # AUTO-DETECT delimiter
            engine="python"    # wajib untuk autodetect
        )
        print(f"Loaded {len(df)} rows")
        return df
    except FileNotFoundError:
        print(f"Error: File '{path}' tidak ditemukan!")
        raise
    except Exception as e:
        print(f"Error loading data: {e}")
        raise