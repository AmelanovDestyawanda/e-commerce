from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle
import pandas as pd
import matplotlib.pyplot as plt

def cluster_rfm(rfm, k=4):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(rfm)

    model = KMeans(n_clusters=k, random_state=42)
    clusters = model.fit_predict(scaled)

    rfm["Cluster"] = clusters
    rfm.to_csv("output/cluster_result.csv")

    with open("models/kmeans.pkl", "wb") as f:
        pickle.dump(model, f)

    return rfm
