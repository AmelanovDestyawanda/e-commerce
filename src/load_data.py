def load_data(path="data/online_retail.csv"):
    print("Loading data...")

    df = pd.read_csv(
        path,
        encoding="latin1",
        sep=None,          # AUTO-DETECT delimiter
        engine="python"    # wajib untuk autodetect
    )
    print("Loaded", len(df), "rows")
    return df
