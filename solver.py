import numpy as np 
from objective_function import get_J, get_U

def get_X(theta, k, wj, N, dt, OMEGA_x, OMEGA_y,OMEGA_z, X0):
    """ Calculate X, Y
    k: index for theta """
    X_k_minus = X0.T
    for i in range (k):
        U = get_U(theta_k= theta[i], wj= wj, dt= dt, OMEGA_x= OMEGA_x, OMEGA_y= OMEGA_y, OMEGA_z= OMEGA_z)
        X_k_minus = U @ X_k_minus
    return X_k_minus



def get_Y(theta, k, wj, N, dt, OMEGA_x, OMEGA_y,OMEGA_z, Yt):
    """ Calculate X, Y 
    k: index for theta"""
    n = len(theta)
    Y_k_plus = Yt
    for i in reversed(range(n-k, n)):
        U = get_U(theta_k= theta[n-i], wj= wj, dt= dt, OMEGA_x= OMEGA_x, OMEGA_y= OMEGA_y, OMEGA_z= OMEGA_z)
        Y_k_plus = Y_k_plus @ U
    return Y_k_plus



def get_e_k(theta, k, w, N, dt, OMEGA_x, OMEGA_y,OMEGA_z, Yt, X0):
    """ Calculate e """
    
    e =0
    for count in range(N):
        X_k = get_X(theta= theta, k= k, wj= w[count], N= N, dt= dt, OMEGA_x= OMEGA_x, OMEGA_y= OMEGA_y,OMEGA_z= OMEGA_z, X0= X0)
        Y_k = get_Y(theta= theta, k= k, wj= w[count], N= N, dt= dt, OMEGA_x= OMEGA_x, OMEGA_y= OMEGA_y,OMEGA_z= OMEGA_z, Yt= Yt)
        e += np.cross (X_k, Y_k)
    return e


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

    print('Testing Funtion : X,Y \n\
        test case inputs    output =')
    print('for wj=', w[0])
    print('function: get_x[3]:'\
        ,get_X(theta = intial_theta, k =3, wj= w[0], N = N, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y,OMEGA_z = OMEGA_z, X0 = X0))
    print()
    print()
    print('function: get_y[3]:',get_Y(theta = intial_theta, k =3,  wj= w[0], N = N, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y,OMEGA_z = OMEGA_z, Yt = Yt))


    print('Testing Funtion : e \n\
        test case inputs    output =')
    print('function: get_e[3]:'\
    ,get_e_k(theta = intial_theta, k =3, w = w, N = N, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y,OMEGA_z = OMEGA_z, X0 = X0, Yt= Yt))
