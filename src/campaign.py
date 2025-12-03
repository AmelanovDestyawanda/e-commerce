import pandas as pd

def generate_campaign_recommendations(file_path="output/cluster_result.csv"):
    """
    Membaca hasil clustering dan memberikan rekomendasi aksi marketing
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        return None

    # Fungsi mapping label berdasarkan analisis karakteristik cluster
    def get_segment_label(cluster):
        if cluster == 2:
            return "Whales (VIP)"
        elif cluster == 3:
            return "Loyal Champions"
        elif cluster == 0:
            return "Regular Active"
        elif cluster == 1:
            return "Risk of Churn"
        return "Unknown"

    # Fungsi mapping rekomendasi aksi
    def get_action(cluster):
        if cluster == 2:
            return "Assign Personal Manager & Early Access"
        elif cluster == 3:
            return "Send Loyalty Reward & Referral Bonus"
        elif cluster == 0:
            return "Product Recommendation Email (Cross-sell)"
        elif cluster == 1:
            return "Send 'We Miss You' 20% Discount Code"
        return "N/A"

    # Terapkan logic
    df["Segment_Name"] = df["Cluster"].apply(get_segment_label)
    df["Recommended_Action"] = df["Cluster"].apply(get_action)

    return df

if __name__ == "__main__":
    # Test run
    df_campaign = generate_campaign_recommendations()
    if df_campaign is not None:
        print(df_campaign[["CustomerID", "Segment_Name", "Recommended_Action"]].head())
        df_campaign.to_csv("output/campaign_target_list.csv", index=False)
        print("Campaign list saved to output/campaign_target_list.csv")