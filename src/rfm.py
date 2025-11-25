import pandas as pd
from datetime import timedelta

def create_rfm(df):

    ref_date = df['InvoiceDate'].max() + timedelta(days=1)

    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (ref_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalPrice': 'sum'
    })

    rfm.columns = ['Recency', 'Frequency', 'Monetary']
    return rfm
