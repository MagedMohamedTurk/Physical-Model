
import numpy as np 
from math import pi
from solver import standard_solver
import tools

""" Inputs 
We shall start with test case parameters
"""

#n = 10 # Number of thetas

B = 3
j = 10 # Assumed number of random w over [B, -B]
T = 20*pi
N = 300 # Number of thetas
X0 = [0,0,1]
Yt = [1,0,0]


OMEGA_x = [
    [0, 0, 0],
    [0, 0, -1],
    [0, 1, 0]]

OMEGA_y = [
    [0, 0, 1],
    [0, 0, 0],
    [-1,0, 0]]

OMEGA_z = [
    [0, -1, 0],
    [1, 0, 0],
    [0, 0, 0]]

OMEGA_x = tools.convert_numpy(OMEGA_x)
OMEGA_y = tools.convert_numpy(OMEGA_y)
OMEGA_z = tools.convert_numpy(OMEGA_z)

#convert X0, Yt into numpy array (1X3 vectors)
X0 = tools.convert_numpy(X0)
Yt = tools.convert_numpy(Yt)



intial_theta = np.zeros(N)
w = tools.get_w(B, j) # Pseudorandom wj
dt = T/N



""" Solve the iterative model  """

results = standard_solver(theta = intial_theta, w= w, N= N, dt= dt, 
                        OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y,
                        OMEGA_z = OMEGA_z )










""" Testing Unit """
print('Intial_thetas:{}'.format(intial_theta),'\n\
    dt =',dt)