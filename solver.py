import numpy as np 
from objective_function import get_J, get_U

def get_X(theta, wj, N, dt, OMEGA_x, OMEGA_y,OMEGA_z, X0):
    """ Calculate X, Y """

    X_k_minus= np.zeros((N-1,3))
    X_k_minus[0] = X0
    for k in range (1,N-1):
        U = get_U(theta_k= theta[k-1], wj= wj, N= N, dt= dt, OMEGA_x= OMEGA_x, OMEGA_y= OMEGA_y, OMEGA_z= OMEGA_z)
        X_k_minus[k] = np.dot(U, X_k_minus[k-1])
    return X_k_minus



def get_Y(theta, wj, N, dt, OMEGA_x, OMEGA_y,OMEGA_z, Yt):
    """ Calculate X, Y """

    Y_k_plus= np.zeros((N+1,3))
    Y_k_plus[-1] = Yt
    for k in reversed(range(N-1)):
        U = get_U(theta_k= theta[k], wj= wj, N= N, dt= dt, OMEGA_x= OMEGA_x, OMEGA_y= OMEGA_y, OMEGA_z= OMEGA_z)
        Y_k_plus[k] = np.dot(Y_k_plus[k+1], U)
    return Y_k_plus



def get_e():
    """ Calculate e """
    X, Y = get_X_Y()
    return


def update_theta ():
    """ update theta """
    e = get_e()
    return


def standard_solver(theta, w, N, dt, OMEGA_x, OMEGA_y, OMEGA_z):
    """ Solving the model
    theta = list(n) of theta values
    w = list(j) of wj
    N = number of piece-wise elements over time T
    dt = time interval
    OMEGA_x, OMEGA_y, OMEGA_z = .....................
    """
    J = get_J()
    iter_n = 0
    while (float(J) < 0.999) | (float(iter_n) < 1000):
        theta = update_theta()
        J = get_J()
        iter_n += 1
    return











""" Testing Unit """

if __name__ == "__main__":

    print('Testing Funtion : get_X \n\
        test case inputs    output =')
    import tools

    """ Inputs 
    We shall start with test case parameters
    """

    #n = 10 # Number of thetas

    B = 3
    j = 10 # Assumed number of random w over [B, -B]
    T = 20*np.pi
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

    X0 = tools.convert_numpy(X0)
    Yt = tools.convert_numpy(Yt)
   

    intial_theta = np.zeros(N)
    w = tools.get_w(B, j) # Pseudorandom wj
    dt = T/N

    print('function: get_x:',get_X(theta = intial_theta, wj= w[0], N = N, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y,OMEGA_z = OMEGA_z, X0 = X0).shape)
    print('function: get_y:',get_Y(theta = intial_theta, wj= w[0], N = N, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y,OMEGA_z = OMEGA_z, Yt = Yt))