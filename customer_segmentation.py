from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def create_customer_segments(data, n_clusters=4):
    """
    Perform customer segmentation using KMeans clustering.
    Args:
        data (DataFrame): Input customer features.
        n_clusters (int): Number of clusters.
    Returns:
        data (DataFrame): Data with cluster assignments.
    """
    # Standardize data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Apply KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    data['cluster'] = kmeans.fit_predict(scaled_data)
    return data
