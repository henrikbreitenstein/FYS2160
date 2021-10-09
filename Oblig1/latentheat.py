import numpy as np
import matplotlib.pyplot as plt
import termoread as tm

Ta = 22 # celsius
T0 = 90 # celsius
Tm = 63 # celsius

dt = 0.01
tt = np.arange(0, 7000, 0.01)
T = np.zeros(len(tt))
T[0] = T0
for i, t in enumerate(tt[:-1]):
    if T[i] > Tm:
        c = 4
    else:
        c = 0.1
    T[i+1] = T[i] - 0.3*c*(T[i] - Ta)*dt

plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=20)

fig=plt.figure(figsize=(10, 8))
plt.title("Modell for varmetap til det faseskiftende materiale")
plt.xlabel('t [s]')
plt.ylabel('$T [^{\circ} C]$')
plt.plot(tt, T, label='modell')
plt.legend()
plt.show()
