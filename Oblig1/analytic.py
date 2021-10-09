import numpy as np
import matplotlib.pyplot as plt

N = 50
q = np.arange(1, 400)
T = 1/np.log((q+N)/q)
cv = N/T**2*(np.exp(1/T)/(np.exp(1/T)-1)**2)/N
S = (q+N)*np.log(q+N) - q*np.log(q) - N*np.log(N)

plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=20)
fig=plt.figure(figsize=(10, 8))
plt.title("Einstein krystall $N = 50$, Entropi Analytisk")
plt.xlabel('q')
plt.ylabel('$\\frac{S_N}{k_B}$')
plt.plot(q, S)
plt.show()



fig=plt.figure(figsize=(10, 8))
plt.title("Einstein krystall $N = 50$, Varmekapasitet Analytisk")
plt.xlabel('$\\frac{T\\epsilon}{N k_B}$')
plt.ylabel('$\\frac{C\\epsilon}{N k_B}$')
plt.plot(T, cv)
plt.show()
