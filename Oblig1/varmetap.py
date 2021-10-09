import numpy as np
import matplotlib.pyplot as plt
import termoread as tm



plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=16)

fig, axs = plt.subplots(2)
axs[0].scatter(tm.t[100:], np.gradient(tm.T1[100:]))
axs[0].set_title('Varmetap konduksjon Bodum')
axs[1].scatter(tm.t[100:], np.gradient(tm.T2[100:]))
axs[1].set_title('Varmetap konduksjon Temperfect')
for i in (0, 1):
    axs[i].set_xlabel('t [s]')
    axs[i].set_ylabel('$\\frac{\mathrm{d}T}{\mathrm{d}t} \; [^{\circ}C]$')


plt.show()
