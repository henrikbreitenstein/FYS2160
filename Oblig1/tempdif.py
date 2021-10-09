import numpy as np
import matplotlib.pyplot as plt
import termoread as tm

plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=20)
fig=plt.figure(figsize=(10, 8))
plt.title("Temperaturforksjellen mellom Bodum og Temperfect")
plt.xlabel('t [s]')
plt.ylabel('$T_B - T_T \; [^{\circ}C]$')
#plt.plot(tm.t[100:2000], tm.T1[100:2000]-tm.T2[100:2000])
plt.plot(tm.t[100:], tm.T1[100:]-tm.T2[100:])
plt.show()
