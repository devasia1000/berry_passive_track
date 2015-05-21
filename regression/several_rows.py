import json
import matplotlib.pyplot as p
import pylab
import numpy as np

fin1 = open('../data/353918054312018_0.txt', 'r')
fin2 = open('../data/353918054312018_0.txt', 'r')
fin3 = open('../data/353918054312018_0.txt', 'r')

x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

for line in fin1:
    temp = json.loads(line)
    
    x1.append(temp['time'])
    y1.append(temp['lat'])

mean_x1 = sum(x1)/float(len(x1))
mean_y1 = sum(y1)/float(len(y1))

for i in range(0, len(x1)):
    x1[i] = x1[i]-mean_x1
    y1[i] = y1[i]-mean_y1

    x.append(x1[i])
    y.append(y1[i])

for line in fin2:
    temp = json.loads(line)
    
    x2.append(temp['time'])
    y2.append(temp['lat'])

mean_x2 = sum(x2)/float(len(x2))
mean_y2 = sum(y2)/float(len(y2))

for i in range(0, len(x2)):
    x2[i] = x2[i]-mean_x2
    y2[i] = y2[i]-mean_y2-0.003

    x.append(x2[i])
    y.append(y2[i])






for line in fin3:
    temp = json.loads(line)
    
    x3.append(temp['time'])
    y3.append(temp['lat'])

mean_x3 = sum(x3)/float(len(x3))
mean_y3 = sum(y3)/float(len(y3))

for i in range(0, len(x3)):
    x3[i] = x3[i]-mean_x3
    y3[i] = y3[i]-mean_y3-(x3[i]/1000000 + 0.003)

    x.append(x3[i])
    y.append(y3[i])



    
m,b = np.polyfit(x, y, 1)
print m, b

eval_y = []
for val in x:
    eval_y.append(m*val+b)


p.figure()

p.plot(x1, y1, 'g', label='Picker 1')
p.plot(x2, y2, 'g', label='Picker 2')
p.plot(x3, y3, 'g', label='Picker 3')
p.plot(x, eval_y, 'r', label='Picking Slope')

p.legend()
p.show()
