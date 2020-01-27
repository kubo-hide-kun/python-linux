# -*-coding: utf-8-*-

import numpy as np
import matplotlib.pylab as plt

data = np.genfromtxt('data.txt', delimiter=',', dtype='float')
data = data[1:]

datalen = len(data)
print('datalen = ' + str(datalen) + '¥n')

t = []
u = []
y = []

for i in range(dastalen):
    t.append(data[i,1])
    u.append(data[i,2])
    y.append(data[i,3])

plt.plot(t, u, label='u', color='red')
plt.plot(t, y, label='y', color='blue')

plt.grid(True)
plt.xlabel('t[s]')
plt.ylabel('y[V], y[V]')
plt.title('FIG.1 t-u,y')
plt.xlim([0,20])

plt.legend()

plt.show()
f.close()