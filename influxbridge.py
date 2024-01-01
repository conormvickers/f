# pip install influxdb-client

from datetime import datetime
import os

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = os.getenv("INFLUX_TOKEN")
org = "conor"
bucket = "bboi"

with InfluxDBClient(url="http://192.168.50.205:8086", token=token, org=org) as client:



    #send

    write_api = client.write_api(write_options=SYNCHRONOUS)

    data = "mem,host=host1 used_percent=23.43234543"
    write_api.write(bucket, org, data)
    
    #or-------
    point = Point("mem") \
        .tag("host", "host1") \
        .field("used_percent", 23.43234543) \
        .time(datetime.utcnow(), WritePrecision.NS)

    write_api.write(bucket, org, point)
# -----
    client.close()