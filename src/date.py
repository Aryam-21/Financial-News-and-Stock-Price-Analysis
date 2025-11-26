import pandas as pd
def normalize_dates(data_date):
    return pd.to_datetime(data_date, errors='coerce').dt.date
    