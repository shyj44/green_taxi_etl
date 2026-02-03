import pandas as pd

BASE_URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/"

def load_data():
    dfs = []

    for month in ["10", "11", "12"]:
        url = f"{BASE_URL}green_tripdata_2020-{month}.csv.gz"
        df = pd.read_csv(
            url,
            compression="gzip",
            parse_dates=["lpep_pickup_datetime", "lpep_dropoff_datetime"]
        )
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)
