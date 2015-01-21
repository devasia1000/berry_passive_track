import json

clam_data = []

f = open('clam_data.txt', 'r')
for line in f:
    t = json.loads(line)
    print t
