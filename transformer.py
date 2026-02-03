def transform(data):
    data = data[
        (data["passenger_count"] > 0) &
        (data["trip_distance"] > 0)
    ]

    data["lpep_pickup_date"] = data["lpep_pickup_datetime"].dt.date

    data = data.rename(columns={
        "VendorID": "vendor_id",
        "RatecodeID": "ratecode_id",
        "PULocationID": "pu_location_id",
        "DOLocationID": "do_location_id"
    })

    assert data["vendor_id"].isin([1, 2]).all()
    assert (data["passenger_count"] > 0).all()
    assert (data["trip_distance"] > 0).all()

    return data
