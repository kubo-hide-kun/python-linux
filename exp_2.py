# -*-coding: utf-8-*-

import numpy as np
import matplotlib.pylab as plt
import math

f = open('sin.txt','w')

x = np.linspace(-np.pi,np.pi,40)
y = []

for i in range(len(x)):
    y.append(math.sin(x[i]))
    f.write(format(x[i],'8.5f')+','+format(y[i],'8.5f')+'¥n')

plt.plot(x,y,label='y=sin(x)', color='blue', marker='o')

plt.grid(True)
plt.xlabel('t[rad]')
plt.ylabel('y[-]')
plt.title('FIG.2 x-y')

plt.legend()

plt.show()
f.close()