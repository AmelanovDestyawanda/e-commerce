import os
import sys

# Pastikan path src/ bisa diakses
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.load_data import load_data
from src.preprocess import clean_data
from src.rfm import calculate_rfm
from src.clustering import cluster_rfm
from src.visualization import elbow_method

def main():
    """
    Pipeline utama untuk RFM Analysis dan Customer Segmentation
    """
    # Buat folder output dan models jika belum ada
    os.makedirs("output", exist_ok=True)
    os.makedirs("models", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    
    print("="*60)
    print("RFM ANALYSIS & CUSTOMER SEGMENTATION")
    print("="*60)
    
    # 1. Load data
    print("\n[1/5] Loading data...")
    try:
        df = load_data()
        print(f"✓ Data loaded: {len(df)} rows, {len(df.columns)} columns")
    except FileNotFoundError:
        print(" Error: File 'data/online_retail.csv' tidak ditemukan!")
        print("\nPastikan file CSV Anda ada di folder 'data/' dengan nama 'online_retail.csv'")
        print("Atau ubah path di src/load_data.py")
        return
    except Exception as e:
        print(f" Error loading data: {e}")
        return

    # 2. Clean data
    print("\n[2/5] Cleaning data...")
    try:
        df_original = len(df)
        df = clean_data(df)
        print(f"✓ Data cleaned: {len(df)} rows remaining ({df_original - len(df)} rows removed)")
    except Exception as e:
        print(f" Error cleaning data: {e}")
        return

    # 3. Calculate RFM
    print("\n[3/5] Calculating RFM metrics...")
    try:
        rfm = calculate_rfm(df)
        print(f"✓ RFM calculated for {len(rfm)} customers")
        print(f"  - Recency range: {rfm['Recency'].min()}-{rfm['Recency'].max()} days")
        print(f"  - Frequency range: {rfm['Frequency'].min()}-{rfm['Frequency'].max()} transactions")
        print(f"  - Monetary range: ${rfm['Monetary'].min():.2f}-${rfm['Monetary'].max():.2f}")
    except Exception as e:
        print(f" Error calculating RFM: {e}")
        return

    # 4. Elbow method
    print("\n[4/5] Running elbow method to find optimal K...")
    try:
        elbow_method(rfm[["Recency", "Frequency", "Monetary"]])
        print("✓ Elbow plot saved to output/elbow_plot.png")
        print("\n Tip: Lihat grafik elbow untuk menentukan jumlah cluster optimal")
        print("   Cari 'siku' pada grafik dimana penurunan WCSS mulai melambat")
    except Exception as e:
        print(f" Error creating elbow plot: {e}")
        return

    # 5. Clustering
    print("\n[5/5] Performing K-Means clustering...")
    try:
        while True:
            try:
                k_input = input("\nMasukkan jumlah cluster K (recommended: 3-5, default=4): ").strip()
                if k_input == "":
                    k = 4
                else:
                    k = int(k_input)
                
                if k < 2:
                    print(" Jumlah cluster minimal adalah 2. Coba lagi.")
                    continue
                elif k > 10:
                    print(" Jumlah cluster terlalu banyak (max 10). Coba lagi.")
                    continue
                else:
                    break
            except ValueError:
                print(" Input tidak valid. Masukkan angka!")
        
        rfm = cluster_rfm(rfm, k=k)
        print(f"\n✓ Clustering completed with K={k}")
        
    except KeyboardInterrupt:
        print("\n\n Process interrupted by user")
        return
    except Exception as e:
        print(f" Error during clustering: {e}")
        return

    # Summary
    print("\n" + "="*60)
    print(" PROCESS COMPLETED SUCCESSFULLY!")
    print("="*60)
    print("\n Output files:")
    print("   output/rfm_table.csv          - RFM metrics per customer")
    print("   output/cluster_result.csv     - Customer segments")
    print("   output/elbow_plot.png         - Elbow method visualization")
    print("   output/cluster_plot.png       - Cluster visualization")
    print("   models/kmeans.pkl             - Trained K-Means model + scaler")
    
    print("\n Next steps:")
    print("  1. Analisis karakteristik setiap cluster di output/cluster_result.csv")
    print("  2. Beri nama segment (contoh: Champions, Loyal, At Risk, Lost)")
    print("  3. Gunakan predict.py untuk prediksi customer baru")
    print("  4. Deploy dengan api.py untuk production use")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Process interrupted by user")
    except Exception as e:
        print(f"\n Unexpected error: {e}")
        import traceback
        traceback.print_exc()