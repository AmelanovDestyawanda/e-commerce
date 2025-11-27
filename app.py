from src.load_data import load_data
from src.preprocess import clean_data
from src.rfm import calculate_rfm
from src.clustering import cluster_rfm
from src.visualization import elbow_method

def main():
    print("Loading data...")
    df = load_data()

    print("Cleaning...")
    df = clean_data(df)

    print("Calculating RFM...")
    rfm = calculate_rfm(df)

    print("Elbow plot...")
    elbow_method(rfm[["Recency", "Frequency", "Monetary"]])

    print("Clustering...")
    cluster_rfm(rfm)

    print("Done! Check folder output/ and models/")

if __name__ == "__main__":
    main()
