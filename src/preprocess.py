import pandas as pd

def clean_data(df):
    """
    Membersihkan data transaksi e-commerce
    """
    print(f"  - Data awal: {len(df)} rows")
    
    # Hapus baris dengan CustomerID kosong
    df = df.dropna(subset=["CustomerID"])
    print(f"  - Setelah hapus CustomerID null: {len(df)} rows")
    
    # Konversi InvoiceDate ke datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors='coerce')
    
    # Hapus baris dengan InvoiceDate invalid
    df = df.dropna(subset=["InvoiceDate"])
    print(f"  - Setelah hapus InvoiceDate invalid: {len(df)} rows")
    
    # Hitung TotalPrice
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
    
    # Filter hanya transaksi dengan Quantity > 0 (hapus return/refund)
    df = df[df["Quantity"] > 0]
    print(f"  - Setelah filter Quantity > 0: {len(df)} rows")
    
    # Filter hanya transaksi dengan UnitPrice > 0
    df = df[df["UnitPrice"] > 0]
    print(f"  - Setelah filter UnitPrice > 0: {len(df)} rows")
    
    # Hapus duplikat
    df = df.drop_duplicates()
    print(f"  - Setelah hapus duplikat: {len(df)} rows")
    
    return df