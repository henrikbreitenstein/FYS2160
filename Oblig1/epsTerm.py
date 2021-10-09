import numpy as np
import matplotlib.pyplot as plt
import termoread as tm




plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=20)

Ta = 22 #celcius
T0 = 80 #celsius
tau = 4670.5
ttau1 = 200
ttau2 = 400
Tm1 = 61 #celsius
dTm1 = (Tm1-Ta)/(T0-Ta)
Tnorm = 59 #celsius
dTm2 = (Tnorm-Ta)/(T0-Ta)
eps = 1e-6
run = 0

def cv(T):
    return 1/T**2*(np.exp(1/T)/(np.exp(1/T)-1)**2)

N = 500
qmaks = N*5
q = np.linspace(1, qmaks, 5*qmaks)
T = 1/np.log((q+N)/q)
cv1 = cv(T)
q099 = q[np.where(abs(cv1 - 0.99) < 1e-4)[0][0]]
it1= np.where(abs(tm.T2-Tm1)<1e-3)[0][0]
it2 = np.where(abs(tm.T2-Tnorm)<1e-3)[0][0]
q1 = np.linspace(1, q099, it1)
q2 = np.linspace(1, q099, it2)
T1 = 1/np.log((q1+N)/q1)
T2 = 1/np.log((q2+N)/q2)
cv2 = cv(T1)
cv3 = cv(T2)
Ttau1 = [dTm1 + (1- dTm1)*np.exp(-tm.t[i]/(cv2[i]*ttau1)) for i in \
range(it1)]
Ttau2 = [dTm2  + (Ttau1[-1]-dTm2)*np.exp(-tm.t[i-it1]/(cv3[i-it1]*ttau2)) \
for i in range(it1, it2, 1)]
Ttau0 = np.exp(-tm.t[it2:]/tau)
Ttau0 = Ttau0 + (Ttau2[-1] - Ttau0[0])
Tf = []
Tf = Tf + Ttau1
Tf = Tf + Ttau2
Ttau0 = list(Ttau0)
Tf = Tf + Ttau0
Ttest = np.exp(-tm.t/tau)
fig=plt.figure(figsize=(10, 8))
plt.title("Modell med varmekapasitet for einsteinkrystall")
plt.xlabel('t [s]')
plt.ylabel('$\Delta T \ \Delta T_0$')
dT2 = (tm.T2 - Ta)/(T0-Ta)
plt.plot(tm.t, dT2, label='data', lw=1)
plt.plot(tm.t, Tf, label='model', lw=3)
plt.legend()
plt.show()
