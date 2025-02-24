import matplotlib.pyplot as plt

def compare_clusters(kmeans_df, dbscan_df):
    """
    Compare K-Means and DBSCAN clustering results.
    
    Parameters:
        kmeans_df (pd.DataFrame): K-Means clustering results.
        dbscan_df (pd.DataFrame): DBSCAN clustering results.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # K-Means visualization
    kmeans_df.plot.scatter(x='avg_gap', y='total_doses', c='cluster', cmap='viridis', 
                          ax=ax1, title='K-Means Clustering')
    
    # DBSCAN visualization
    dbscan_df.plot.scatter(x='avg_gap', y='total_doses', c='cluster', cmap='viridis',
                          ax=ax2, title='DBSCAN Clustering')
    
    plt.show()

    # Statistical comparison
    print("K-Means Cluster Stats:")
    print(kmeans_df.groupby('cluster').describe())
    print("\nDBSCAN Cluster Stats:")
    print(dbscan_df.groupby('cluster').describe())