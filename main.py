
import numpy as np 
from math import pi
from solver import standard_solver
import tools

""" Inputs 
We shall start with test case parameters
"""


B = 3
T = 20*np.pi
N = 300 # Number random frequencies wj over [B, -B]
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




w = tools.get_w(B, N) # Pseudorandom wj
n = 20 # assume number of thetas
dt= T/n 
intial_theta = np.zeros(n)


B = 3
T = 20*np.pi
N = 300 # Number random frequencies wj over [B, -B]
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




w = tools.get_w(B, N) # Pseudorandom wj
n = 20 # assume number of thetas
dt= T/n 
intial_theta = np.zeros(n)

""" Solve the iterative model  """

print('Testing Funtion : standard_solver() \n\
    test case inputs    output =')
print('function: update_theta(intial_theta):'\
,  standard_solver(intial_theta = intial_theta, w= w, N= N, dt= dt, OMEGA_x= OMEGA_x, OMEGA_y= OMEGA_y, OMEGA_z= OMEGA_z, X0= X0, Yt= Yt))