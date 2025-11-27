import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def elbow_method(data):
    wcss = []
    for k in range(1, 11):
        km = KMeans(n_clusters=k)
        km.fit(data)
        wcss.append(km.inertia_)

    plt.plot(range(1, 11), wcss, marker="o")
    plt.title("Elbow Method")
    plt.xlabel("Clusters")
    plt.ylabel("WCSS")
    plt.savefig("output/elbow_plot.png")
