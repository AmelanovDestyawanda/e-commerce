import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def elbow_method(data, max_k=11):
    """
    Elbow method untuk menentukan jumlah cluster optimal
    """
    # Standardisasi data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    wcss = []
    k_range = range(1, max_k)
    
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(scaled_data)
        wcss.append(km.inertia_)

    # Plot elbow
    plt.figure(figsize=(10, 6))
    plt.plot(k_range, wcss, marker="o", linestyle="-", linewidth=2, markersize=8)
    plt.title("Elbow Method - Optimal K Clusters", fontsize=14, fontweight="bold")
    plt.xlabel("Number of Clusters (K)", fontsize=12)
    plt.ylabel("WCSS (Within-Cluster Sum of Squares)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(k_range)
    
    # Tambahkan anotasi
    for i, (k, w) in enumerate(zip(k_range, wcss)):
        if i % 2 == 0:  # Tampilkan setiap 2 titik
            plt.annotate(f'{w:.0f}', xy=(k, w), 
                        xytext=(5, 5), textcoords='offset points',
                        fontsize=9, alpha=0.7)
    
    plt.tight_layout()
    plt.savefig("output/elbow_plot.png", dpi=300, bbox_inches="tight")
    print("Elbow plot saved to output/elbow_plot.png")
    print("\nAnalisis grafik elbow untuk menentukan K optimal.")
    print("Cari 'siku' pada grafik dimana penurunan WCSS mulai melambat.")
    plt.close()