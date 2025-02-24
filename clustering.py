from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
import os

# Fix memory leak warning on Windows
os.environ['OMP_NUM_THREADS'] = '1'

def cluster_kmeans(data, n_clusters=3):
    """
    Perform K-Means clustering on adherence metrics.
    
    Parameters:
        data (pd.DataFrame): Adherence metrics.
        n_clusters (int): Number of clusters.
    
    Returns:
        pd.DataFrame: Data with cluster labels.
    """
    scaler = StandardScaler()
    scaled = scaler.fit_transform(data)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    data = data.copy()
    data.loc[:, 'cluster'] = kmeans.fit_predict(scaled)
    return data

def cluster_dbscan(data, eps=0.5):
    """
    Perform DBSCAN clustering on adherence metrics.
    
    Parameters:
        data (pd.DataFrame): Adherence metrics.
        eps (float): Maximum distance between two samples for them to be considered neighbors.
    
    Returns:
        pd.DataFrame: Data with cluster labels.
    """
    scaler = StandardScaler()
    scaled = scaler.fit_transform(data)
    dbscan = DBSCAN(eps=eps)
    data = data.copy()
    data.loc[:, 'cluster'] = dbscan.fit_predict(scaled)
    return data