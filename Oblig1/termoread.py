import numpy as np

K = 273
Ta = 22 + K

t, T1, T2 = np.loadtxt('termokopper.txt', unpack=True)
