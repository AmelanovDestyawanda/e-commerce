import matplotlib.pyplot as plt
import seaborn as sns

def cluster_plot(rfm):
    plt.figure(figsize=(6,4))
    sns.scatterplot(
        x=rfm['Recency'],
        y=rfm['Monetary'],
        hue=rfm['Cluster'],
        palette='tab10'
    )
    plt.savefig('output/plots/rfm_clusters.png')
