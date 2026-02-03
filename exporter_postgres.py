from sqlalchemy import create_engine

def export_to_postgres(data):
    engine = create_engine(
        "postgresql://user:password@localhost:5432/dbname"
    )

    data.to_sql(
        "green_taxi",
        engine,
        schema="mage",
        if_exists="replace",
        index=False
    )
