from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle
import pandas as pd
import matplotlib.pyplot as plt

def cluster_rfm(rfm, k=4):
    """
    Clustering RFM menggunakan K-Means
    """
    # Standardisasi data
    scaler = StandardScaler()
    scaled = scaler.fit_transform(rfm[["Recency", "Frequency", "Monetary"]])

    # K-Means clustering
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    clusters = model.fit_predict(scaled)

    # Tambahkan cluster ke dataframe
    rfm["Cluster"] = clusters
    
    # Simpan hasil
    rfm.to_csv("output/cluster_result.csv", index=True)

    # Simpan model dan scaler
    with open("models/kmeans.pkl", "wb") as f:
        pickle.dump({"model": model, "scaler": scaler}, f)

    # Visualisasi cluster
    visualize_clusters(rfm)
    
    # Tampilkan statistik per cluster
    print("\n=== Statistik per Cluster ===")
    cluster_stats = rfm.groupby("Cluster").agg({
        "Recency": ["mean", "min", "max"],
        "Frequency": ["mean", "min", "max"],
        "Monetary": ["mean", "min", "max"]
    }).round(2)
    print(cluster_stats)
    
    # Hitung jumlah customer per cluster
    print("\n=== Jumlah Customer per Cluster ===")
    print(rfm["Cluster"].value_counts().sort_index())

    return rfm


def visualize_clusters(rfm):
    """
    Visualisasi hasil clustering dalam 3 panel
    """
    fig = plt.figure(figsize=(15, 5))
    
    # Plot 1: Recency vs Frequency
    ax1 = fig.add_subplot(131)
    scatter1 = ax1.scatter(rfm["Recency"], rfm["Frequency"], 
                          c=rfm["Cluster"], cmap="viridis", alpha=0.6)
    ax1.set_xlabel("Recency (days)")
    ax1.set_ylabel("Frequency")
    ax1.set_title("Recency vs Frequency")
    plt.colorbar(scatter1, ax=ax1, label="Cluster")
    
    # Plot 2: Frequency vs Monetary
    ax2 = fig.add_subplot(132)
    scatter2 = ax2.scatter(rfm["Frequency"], rfm["Monetary"], 
                          c=rfm["Cluster"], cmap="viridis", alpha=0.6)
    ax2.set_xlabel("Frequency")
    ax2.set_ylabel("Monetary")
    ax2.set_title("Frequency vs Monetary")
    plt.colorbar(scatter2, ax=ax2, label="Cluster")
    
    # Plot 3: Recency vs Monetary
    ax3 = fig.add_subplot(133)
    scatter3 = ax3.scatter(rfm["Recency"], rfm["Monetary"], 
                          c=rfm["Cluster"], cmap="viridis", alpha=0.6)
    ax3.set_xlabel("Recency (days)")
    ax3.set_ylabel("Monetary")
    ax3.set_title("Recency vs Monetary")
    plt.colorbar(scatter3, ax=ax3, label="Cluster")
    
    plt.tight_layout()
    plt.savefig("output/cluster_plot.png", dpi=300, bbox_inches="tight")
    print("Cluster plot saved to output/cluster_plot.png")
    plt.close()