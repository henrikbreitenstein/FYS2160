import termoread as tm
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt


plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=20)
fig=plt.figure(figsize=(10, 8))

Ta = 22
dT = (tm.T1 - Ta)/(np.amax(tm.T1) - Ta)
tau = tm.t[np.where(abs(dT-np.exp(-1)) < 1e-4)[0][0]]
print(tau)
dTmodelfunc = lambda x : np.exp(-x/tau)
dtmodel = dTmodelfunc(tm.t)
plt.title(f'Modell med tilnærmet $\\tau = {tau} \; s$')
plt.xlabel('t [s]')
plt.ylabel('$\Delta T \ \Delta T_0$')
plt.plot(tm.t[100:], dT[100:], label='data')
plt.plot(tm.t[100:], dtmodel[100:], label='model')
plt.legend()
plt.show()
