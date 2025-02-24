import numpy as np
import pandas as pd

def calculate_adherence(df):
    """
    Calculate adherence metrics for each patient.
    
    Parameters:
        df (pd.DataFrame): Medication data.
    
    Returns:
        pd.DataFrame: Adherence metrics.
    """
    grouped = df.groupby('PATIENT_ID')['DATE']
    adherence = {}
    for pid, dates in grouped:
        dates = sorted(dates)  # Ensure dates are sorted
        gaps = [(dates[i + 1] - dates[i]).days for i in range(len(dates) - 1)]
        adherence[pid] = {
            'total_doses': len(dates),
            'avg_gap': np.mean(gaps),
            'regimen_complexity': len(df[df.PATIENT_ID == pid].CATEGORY.unique())
        }
    return pd.DataFrame(adherence).T.reset_index()