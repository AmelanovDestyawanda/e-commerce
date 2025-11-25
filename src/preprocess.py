import pandas as pd

def preprocess_data(path):
    df = pd.read_csv(path)

    # Hapus transaksi return
    df = df[df['Quantity'] > 0]

    # Hapus CustomerID kosong
    df = df.dropna(subset=['CustomerID'])

    # Konversi tanggal
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # Hitung total harga
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    return df
