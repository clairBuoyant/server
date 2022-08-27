from datetime import datetime as dt

from pybuoy import Buoy

buoy = Buoy()
STATION_ID = "44065"

data = buoy.realtime.get(station_id=STATION_ID, dataset="spec")

rows = data.strip().split("\n")
headers = [" ".join(row.split()).split(" ") for row in rows[0:2]]
for row in rows[2:]:
    record_array = " ".join(row.split()).split(" ")
    date_recorded = dt(
        int(record_array[0]),
        int(record_array[1]),
        int(record_array[2]),
        int(record_array[3]),
        int(record_array[4]),
    )

# There are 15 header columns. 0 to 4 must be turned into date time
# print(clean_data[0:4])
