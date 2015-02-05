import json
import datetime

clam_data = []

#time_offset = 45
#lat_offset = 23.3451738
#lon_offset = -42.462398

time_offset = 0
lat_offset = 0
lon_offset = 0

prev_day = 0
count = 0

f = open('clam_data.txt', 'r')
for line in f:
    t = json.loads(line)
    if prev_day == 0:
    	prev_day = datetime.datetime.fromtimestamp(int(t['time'])).strftime('%Y-%m-%d')
    
    day = datetime.datetime.fromtimestamp(int(t['time'])).strftime('%Y-%m-%d')
    if day != prev_day:
    	count = count + 1
    	prev_day = day
    


    new_data = dict()
    new_data['time'] = t['time']
    new_data['day_number'] = count
    new_data['imei'] = t['imei']
    new_data['lat'] = t['lat']
    new_data['lon'] = t['lon']
    
    print json.dumps(new_data)

    #print new_data

    #print t['time'] + time_offset, ',', t['imei'], ',', t['lat'] + lat_offset, ',', t['lon'] + lon_offset
