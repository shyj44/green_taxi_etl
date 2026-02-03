import pyarrow as pa
import pyarrow.parquet as pq

def export_to_gcp(data):
    table = pa.Table.from_pandas(data)

    pq.write_to_dataset(
        table,
        root_path="gs://your-bucket/green_taxi",
        partition_cols=["lpep_pickup_date"]
    )
