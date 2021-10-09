import numpy as np
import matplotlib.pyplot as plt
import termoread as tm
import scipy.optimize as sco

plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=20)

Ta = 22 #celcius
Tm = 61 #celcius
T0 = 80 #celsius
tau = 4670.5/4
dTchange = (Tm-Ta)/(T0-Ta)
Ttau1 = np.exp(-tm.t/(0.1*tau))
dTchange_i = np.where(abs(Ttau1 - dTchange) < 1e-3)[0][0]
C = dTchange/np.exp(-tm.t[dTchange_i]/(4*tau))
Ttau2 = C*np.exp(-tm.t[dTchange_i:]/(4*tau))
T = np.append(Ttau1[:dTchange_i], Ttau2)

fig=plt.figure(figsize=(10, 8))
plt.title("Modell med $\\tau_1$ og $\\tau_2$")
plt.xlabel('t [s]')
plt.ylabel('$\Delta T \ \Delta T_0$')
plt.plot(tm.t, T, label='model')
plt.legend()
plt.show()
