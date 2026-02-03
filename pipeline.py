from data_loader import load_data
from transformer import transform
from exporter_postgres import export_to_postgres
from exporter_gcp import export_to_gcp

def run_pipeline():
    data = load_data()
    data = transform(data)
    export_to_postgres(data)
    export_to_gcp(data)

if __name__ == "__main__":
    run_pipeline()
