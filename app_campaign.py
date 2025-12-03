import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.campaign import generate_campaign_recommendations

st.set_page_config(page_title="Marketing Campaign System", layout="wide")

st.title("🎯 Sistem Target Kampanye Pemasaran")
st.markdown("Otomasi strategi marketing berdasarkan segmentasi pelanggan RFM.")

# 1. Load Data
df = generate_campaign_recommendations()

if df is not None:
    # 2. Metrics Summary
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Pelanggan", len(df))
    col2.metric("Pelanggan VIP", len(df[df["Cluster"]==2]))
    col3.metric("Pelanggan Loyal", len(df[df["Cluster"]==3]))
    col4.metric("Berisiko Churn", len(df[df["Cluster"]==1]))

    st.markdown("---")

    # 3. Filter Segment
    selected_segment = st.selectbox(
        "Pilih Segmen untuk Melihat Detail:",
        ["All", "Whales (VIP)", "Loyal Champions", "Regular Active", "Risk of Churn"]
    )

    if selected_segment != "All":
        filtered_df = df[df["Segment_Name"] == selected_segment]
    else:
        filtered_df = df

    # 4. Tampilkan Tabel
    st.subheader(f"Daftar Target: {selected_segment}")
    st.dataframe(filtered_df[["CustomerID", "Recency", "Frequency", "Monetary", "Recommended_Action"]])

    # 5. Simulasi Kirim Email
    st.markdown("### 📧 Action Zone")
    if st.button(f"Kirim Kampanye ke {len(filtered_df)} Pelanggan ini"):
        st.success(f"Berhasil! Email kampanye '{filtered_df.iloc[0]['Recommended_Action']}' sedang dikirim ke {len(filtered_df)} pelanggan.")
        
else:
    st.error("File output/cluster_result.csv tidak ditemukan. Jalankan analisis clustering terlebih dahulu.")