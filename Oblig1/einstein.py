import numpy as np
import matplotlib.pyplot as plt

def fc(n, yn):
    if yn==0:
        return np.math.factorial(n)
    else:
        a = np.sqrt(2*np.pi*n)
        b = np.power(n/np.exp(1), n)
        return a*b

class crystal:
    def __init__(self, q, N):
        self.q = q
        self.N = N
        self.run = np.array([0,0,0,0])

    def ohm(self):
        q = self.q; N = self.N
        yq = 1 if q>500 else 0
        yn = 1 if N>500 else 0
        y = 1 if (N+q)>1000 else 0
        mult = fc(N-1+q, y)/(fc(q, yq)*fc(N-1, yn))
        self.mult = mult
        self.run[0] = 1
        return mult

    def S(self):
        q = self.q; N = self.N
        dummy=self.ohm() if self.run[0]==0 else 0
        self.run[1] = 1
        self.Ent = np.log(self.mult)
        return self.Ent


    def Tder(self):
        q = self.q; N = self.N
        dummy=self.S() if self.run[1]==0 else 0
        self.dcrystal = crystal(q+1, N)
        self.T = abs(1/(self.dcrystal.S() - self.Ent))
        self.run[2] = 1
        return self.T

    def heatcap(self):
        q = self.q; N = self.N
        dummy=self.Tder() if self.run[2]==0 else 0
        self.C = abs(1/(self.dcrystal.Tder() - self.T))
        self.run[3]=1
        return self.C
