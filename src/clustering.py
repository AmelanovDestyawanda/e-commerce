from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle

def run_kmeans(rfm, n_clusters):

    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm)

    model = KMeans(n_clusters=n_clusters, random_state=42)
    labels = model.fit_predict(rfm_scaled)

    rfm['Cluster'] = labels

    # Save model
    with open('models/kmeans.pkl', 'wb') as f:
        pickle.dump(model, f)

    return rfm
