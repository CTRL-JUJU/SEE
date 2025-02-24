import pandas as pd

def load_med_events():
    """
    Load the med.events dataset from CSV.
    
    Returns:
        pd.DataFrame: Medication events data.
    """
    # Load the dataset (ensure the CSV is in the same directory)
    med_events_df = pd.read_csv("med_events.csv")
    
    # Convert DATE column to datetime
    med_events_df['DATE'] = pd.to_datetime(med_events_df['DATE'], format='%m/%d/%Y')
    
    return med_events_df