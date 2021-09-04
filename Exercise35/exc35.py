import numpy as np
import matplotlib.pyplot as plt
import lammps_logfile
from ovito.io import import_file
plt.rc('text', usetex=True) # Setting LaTex fonts and style
plt.rc('font', family='serif', size=16) # as well as the desired text size
'''
Reading Lammps bump file using the ovito enviroment:
If the ovito enviroment is not installed, install using
- Mac OS / Linux : pip install ovito
- Windows : ??
For further information, see: ’https://ovito.org/manual_testing/python/modules/ovito_io’
'''
pipeline = import_file('dump.lammpstrj')
_t = []
_N_atoms = []
_Lx = []
_Ly = []
_x = []
_y = []
_vx = []
_vy = []
for frame in range(pipeline.source.num_frames):
    data = pipeline.compute(frame)
    _Lx.append(data.cell[0,0])
    _Ly.append(data.cell[1,1])
    _t.append(data.attributes['Timestep'])
    _N_atoms.append(data.particles.count)
    pos = data.particles.positions
    _x.append(pos[:,0])
    _y.append(pos[:,1])
    vel = data.particles.velocities
    _vx.append(vel[:,0])
    _vy.append(vel[:,1])

t = np.array(_t)
N_atoms = np.array(_N_atoms)
Lx = np.array(_Lx)
Ly = np.array(_Ly)
x = np.array(_x)
y = np.array(_y)
vx = np.array(_vx)
vy = np.array(_vy)

nleft = np.zeros(len(t))
for i in range(len(t)):
    nleft[i] = np.sum(np.where(x[i,:] < Lx[i]/2))
print(f"Mean number of particles to the left in the box: {np.mean(nleft):.3f} ± {np.std(nleft):.3f}")

fig1 = plt.figure()
ax1 = plt.axes()
ax1.plot(t, nleft)
ax1.set_xlabel('time $t$')
ax1.set_title('Number of particles on the left side of the box')
fig1.tight_layout()
plt.show()
