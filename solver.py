""" Solver module has the solvers possible for the problem
Running this file will run the 'Testing Unit` to test functions"""


# Importing modules

import numpy as np 
from objective_function import get_J, get_U, vector_U
import time
import tools




# Define Functions


def get_X(tensor_U, k, X0):
    """ Calculate X(k-1)
    tensor_U is the tensor (N,n,3,3) we calculate from vector_U function
    X0 : intial condition
    k: index for theta """

    if k !=0:
        tensor_U_X = tensor_U[:, k-1::-1, :, :] # slice tesnor U from 0 to k-1
        X =  tools.np_multi_matmul(tensor_U_X, axis=1) @ X0 
    else:
        X = X0 # for theat[0]
    return X





def get_Y(tensor_U, k, Yt):
    """ Calculate Y(k+1)
    tensor_U is the tensor (N,n,3,3) we calculate from vector_U function
    Yt : Target condition
    k: index for theta """

    if k+1 != tensor_U.shape[1]:
        tensor_U_Y = tensor_U[:, -1:k:-1,:,:] # slice tesnor U from n to k+1
        Y = Yt @ tools.np_multi_matmul(tensor_U_Y, axis=1) 
    else:
        Y = Yt # for theta[n]
    return Y






def get_e_k(tensor_U, k, Yt, X0):
    """ Calculate e
    Cross product of X,Y summation over w 
    tensor_U is the tensor (N,n,3,3) we calculate from vector_U function
    X0 : Intial condition
    Yt : Target condition
    k: index for theta"""

    X_k = get_X(tensor_U = tensor_U, k= k, X0= X0)
    Y_k = get_Y(tensor_U = tensor_U, k= k, Yt= Yt)
    e = sum(np.cross (X_k, Y_k))
    return e




def update_theta (tensor_U, theta, Yt, X0):
    """ update theta 
    tensor_U is the tensor (N,n,3,3) we calculate from vector_U function
    X0 : Intial condition
    Yt : Target condition
    theta: Phase angles"""

    theta_updated = np.zeros(theta.shape) # Broadcast empty matrix

    for count in range(len(theta)):
        e= get_e_k(tensor_U = tensor_U, k= count, Yt= Yt, X0= X0) # Get e for every theta
        np.seterr(divide='ignore') # Ignore intial divide by zero erro
        theta_updated[count] = np.arctan (e[0,1] / e[0,0]) # calculate updated theta
    return theta_updated






def standard_solver(theta, w, N, dt, OMEGA_x, OMEGA_y, OMEGA_z, X0, Yt):
    """ Solving the model
    theta = list(n) of theta values
    w = random frequencies
    N = Number random frequencies wj over [B, -B]
    dt = time interval
    OMEGA_x, OMEGA_y, OMEGA_z: Intial conditions 3x3 matrices
    """
    
    tensor_U = vector_U(theta_k =theta, wj = w, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y, OMEGA_z = OMEGA_z)
    J = sum(Yt @ tools.np_multi_matmul(tensor_U, axis=1) @ X0) / N
    print('Trial #0: J=', J)
    iter_n = 0
    while (J < 0.999) or (iter_n < 1000):
        start_time = time.time()
        theta = update_theta(tensor_U, theta,  Yt= Yt, X0= X0)
        tensor_U = vector_U(theta_k =theta, wj = w, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y, OMEGA_z = OMEGA_z)
        J = sum(Yt @ tools.np_multi_matmul(tensor_U, axis= 1) @ X0) / N
        iter_n += 1
        print('Trial #',iter_n,': J=', J,'          in ', round(time.time()-start_time, 2), 'seconds\n')

    return











""" Testing Unit """

if __name__ == "__main__":

    
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
    tensor_U = vector_U(theta_k =intial_theta, wj = w, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y, OMEGA_z = OMEGA_z)


      
    print('Testing Funtion : get_X, get_Y \n\
        test case inputs    output =')
    print('for wj=', w[0])
    X = get_X(tensor_U, k=3, X0 = X0)
    print('function: get_x[3]:', X[0], 'norm(X)=', np.linalg.norm(X[0]))
    
    print()
    print()
    Y= get_Y(tensor_U, k=3, Yt = Yt)
    print('function: get_y[3]:', Y[0], 'norm(Y)=', np.linalg.norm(Y[0]))
    
  
    print('Testing Funtion : get_e_k() \n\
        test case inputs    output =')
    print('function: get_e[3]:'\
    ,get_e_k(tensor_U= tensor_U, k=3, Yt= Yt, X0= X0))
    

    
    print('Testing Funtion : update_theta() \n\
        test case inputs    output =')

    print('function: update_theta(intial_theta):'\
    ,  update_theta (tensor_U = tensor_U, theta= intial_theta, Yt= Yt, X0= X0))
    

    
   
    print('Testing Funtion : standard_solver() \n\
        test case inputs    output =')
    print('function: update_theta(intial_theta):'\
    ,  standard_solver(theta= intial_theta, w= w, N= N, dt= dt, OMEGA_x= OMEGA_x, OMEGA_y= OMEGA_y, OMEGA_z= OMEGA_z, X0= X0, Yt= Yt))
    """

 


    
    print('choosing theta[10]')
    J_equ4 = 0
    for wj in w:
        X = get_X(theta = intial_theta, k = 10, wj= wj, N = N, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y,OMEGA_z = OMEGA_z, X0 = X0)
        Y = get_Y(theta = intial_theta, k = 10,  wj= wj, N = N, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y,OMEGA_z = OMEGA_z, Yt = Yt)
        U = get_U(theta_k= intial_theta[3], wj = wj, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y ,OMEGA_z = OMEGA_z)
        J_equ4 += Y @ U @ X 
    J_equ4 = 1/N * J_equ4
    J = get_J(theta = intial_theta, w= w, N= N, dt= dt, OMEGA_x= OMEGA_x, OMEGA_y= OMEGA_y, OMEGA_z= OMEGA_z, X0= X0, Yt= Yt) 
    print('calculating J from equ.3 = ' ,J, '\ncalculating J from equ.4= ', J_equ4)
    """