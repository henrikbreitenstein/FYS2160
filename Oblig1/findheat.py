import termoread as tm
import numpy as np


print(np.sum(tm.T1[100:2000]) - np.sum(tm.T2[100:2000]))
