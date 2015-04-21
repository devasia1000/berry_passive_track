import json
import matplotlib.pyplot as p
import pylab
import numpy as np

fin = open('../data/353918054312018_0.txt', 'r')
x = []
y = []
best_fit = []
x_outer = []
y_outer = []
for line in fin:
    temp = json.loads(line)
    x.append(temp['time'])
    y.append(temp['lat'])

m,b = np.polyfit(x, y, 1)

for i in range(0, len(y)):
    #val = y[i]-(m*x[i]+b)
    val =y[i] - m*x[i]+b-0.0001
#    print val
    best_fit.append(val)

for i in range(0, len(best_fit)):
    
    std_dev = np.std(best_fit[i:i+550])
    mean = np.mean(best_fit[i:i+550])

    if best_fit[i] <= mean - std_dev:
        x_outer.append(x[i])
        y_outer.append(best_fit[i])    

p.figure()
p.scatter(x_outer, y_outer, 2, [0.66542]*len(x_outer))
p.plot(x, best_fit, 'r')
#p.plot(x, y)

p.show()
