import pandas as pd

def calculate_rfm(df):
    """
    Menghitung RFM (Recency, Frequency, Monetary) metrics
    """
    # Tanggal referensi (1 hari setelah transaksi terakhir)
    reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)
    print(f"  - Reference date: {reference_date.date()}")

    # Agregasi per CustomerID
    rfm = df.groupby("CustomerID").agg({
        "InvoiceDate": lambda x: (reference_date - x.max()).days,  # Recency
        "InvoiceNo": "nunique",  # Frequency (unique invoices)
        "TotalPrice": "sum"      # Monetary
    })

    # Rename kolom
    rfm.columns = ["Recency", "Frequency", "Monetary"]
    
    # Bulatkan Monetary ke 2 desimal
    rfm["Monetary"] = rfm["Monetary"].round(2)
    
    # Simpan hasil
    rfm.to_csv("output/rfm_table.csv", index=True)
    print(f"  - RFM table saved with {len(rfm)} customers")
    
    # Tampilkan statistik deskriptif
    print("\n  RFM Descriptive Statistics:")
    print(rfm.describe().round(2).to_string())
    
    return rfm