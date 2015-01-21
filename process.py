import json

clam_data = []

time_offset = 45
lat_offset = 23.3451738
lon_offset = -42.462398

f = open('clam_data.txt', 'r')
for line in f:
    t = json.loads(line)
    print t['time'] + time_offset, ',', t['imei'], ',', t['lat'] + lat_offset, ',', t['lon'] + lon_offset
