import termoread as tm
import numpy as np
import matplotlib.pyplot as plt


plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=16)

fig, axs = plt.subplots(2)
axs[0].plot(tm.t[100:], tm.T1[100:])
axs[0].set_title('Kopp 1: Bodum')
axs[1].plot(tm.t[100:], tm.T2[100:])
axs[1].set_title('Kopp 2: Temperfect')
for i in (0, 1):
    axs[i].set_xlabel('t [s]')
    axs[i].set_ylabel('T [C]')


plt.show()
