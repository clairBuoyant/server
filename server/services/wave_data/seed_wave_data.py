from pybuoy import Buoy

buoy = Buoy()
STATION_ID = "44065"

data = buoy.realtime.get(station_id=STATION_ID, dataset="spec")

print(type(data))
