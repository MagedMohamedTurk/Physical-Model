""" This is the main program
Tweek the input parameters to get the best results
"""
# Import Modules
import numpy as np 
from math import pi
from solver import standard_solver, get_X, get_Y, get_e_k
from objective_function import get_J, get_U, vector_U
import tools




""" Inputs 
Test case parameters
"""



B = 3
N = 300 # Number random frequencies wj over [B, -B]

T = 20*np.pi
n = 20 # Assume number of thetas

# Intial Conditions
X0 = [0,0,1]
Yt = [1,0,0]

# OMEGA 3x3 matrices
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

dt= T/n 
intial_theta = np.zeros(n)

""" Solve the iterative model  """


print('Testing Funtion : standard_solver() \n\
    test case inputs:\n\
    w= ', w.T, '\nN= ', N, '\nIntial_theta= ',intial_theta.T,'\ndt= ', dt,'\nOMEGA_x\n', OMEGA_x,'\nOMEGA_y\n', OMEGA_y,'\nOMEGA_z\n', OMEGA_z,'\n\
    output =')
print('function: update_theta(intial_theta):'\
,  standard_solver(theta= intial_theta, w= w, N= N, dt= dt, OMEGA_x= OMEGA_x, OMEGA_y= OMEGA_y, OMEGA_z= OMEGA_z, X0= X0, Yt= Yt))



