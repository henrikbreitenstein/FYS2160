import numpy as np
import matplotlib.pyplot as plt
import einstein as es

qq = np.arange(0, 400)

NN = np.arange(5, 50)

N1 = 5
N2 = 50
clist1 = []
clist2 = []
for q in qq:
    clist1.append(es.crystal(q, N1))
    clist2.append(es.crystal(q, N2))

S1 = [c.S() for c in clist1]
S2 = [c.S() for c in clist2]
T2 = [c.Tder() for c in clist2]
cap1 = [c.heatcap() for c in clist1]
cap2 = [c.heatcap() for c in clist2]

plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=20)

"""fig=plt.figure(figsize=(10, 8))
plt.title("Einstein krystall høy temperatur $N = 5$, Entropi")
plt.xlabel('q')
plt.ylabel('$S [k_B]$')
plt.plot(qq, S1)
plt.show()

fig=plt.figure(figsize=(10, 8))
plt.title("Einstein krystall høy temperatur $N = 5$, varmekapasitet")
plt.xlabel('q')
plt.ylabel('$C [\\frac{\\epsilon}{k_B}]$')
plt.plot(qq, cap1)
plt.show()"""

fig=plt.figure(figsize=(10, 8))
plt.title("Einstein krystall $N = 50$, Entropi")
plt.xlabel('q')
plt.ylabel('$S [k_B]$')
plt.plot(qq, S2)
plt.show()

fig=plt.figure(figsize=(10, 8))
plt.title("Einstein krystall $N = 50$, varmekapasitet")
plt.xlabel('$T [\\frac{\\epsilon}{N k_B}]$')
plt.ylabel('$C [\\frac{\\epsilon}{N k_B}]$')
plt.plot(T2, np.array(cap2)/N2)
plt.show()
