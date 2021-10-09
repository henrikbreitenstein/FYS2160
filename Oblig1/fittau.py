import numpy as np
import matplotlib.pyplot as plt
import termoread as tm
import scipy.optimize as sco

plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=20)


def f(t, tau):
    ret = np.exp(-t/tau)
    return ret

Ta = 22 #celcius
dT = (tm.T1 - Ta)/(np.amax(tm.T1) - Ta)
temp1 = tm.T1[200] - Ta
t1 = tm.t[200]
temp2 = tm.T1[5000] - Ta
t2 = tm.t[5000]
tau = (t2 - t1)/np.log(temp1/temp2)
taupos = np.linspace(0.3*tau, 1.7*tau, 100)
taussd = np.zeros_like(taupos)

for steps, ftau in enumerate(taupos):
    dTmodelfunc = lambda x : np.exp(-x/ftau)
    dtmodel = dTmodelfunc(tm.t)
    taussd[steps] = np.sum(np.square(dT[200:] - dtmodel[200:]))

besttau = taupos[np.where(taussd==np.amin(taussd))]
print(besttau)
tau = besttau
dTmodelfunc = lambda x : np.exp(-x/tau)
dtmodel = dTmodelfunc(tm.t)
fig=plt.figure(figsize=(10, 8))
plt.title('Modell med tau fra regresjon')
plt.xlabel('t [s]')
plt.ylabel('$\Delta T \ \Delta T_0$')
plt.plot(tm.t[100:], dT[100:], label='data')
plt.plot(tm.t[100:], dtmodel[100:], label='model')
plt.legend()
plt.show()
