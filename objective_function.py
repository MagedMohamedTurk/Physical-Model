
""" The module contains the stating problem functions
Running this file will run the 'Testing Unit` to test functions"""


# Import modules
import numpy as np 
from scipy.linalg import expm
import tools








# Define functions

def get_U(theta_k, wj, dt, OMEGA_x, OMEGA_y,OMEGA_z):
    """ Calculate U
    theta_k = theta element
    wj = w element
    dt = time interval
    OMEGA_x, OMEGA_y, OMEGA_z : 3x3 matrices """

    #Broadcast zero matrix
    U = np.zeros((3,3))
    
    # Using Scipy expm to do matrix exponential (critical time function!)
    U = expm(dt * ( wj * OMEGA_z +
                            np.cos(theta_k) * OMEGA_x +
                            np.sin(theta_k) * OMEGA_y
                            )
                    )

    return U

"""Vectorizing U to elemenate for-loops which slow down Numpy module
This will be used to create tensor (N,n,3,3)
that gather all the U values for every w and every theat"""

vector_U = np.vectorize(get_U, signature= '(),(),(),(n,n),(n,n),(n,n)->(n,n)')










""" This function is for expermenting here, the function is recalculate in the solver.py module
from the tensor. The point to save time not to call the U values more than once for calculating J once and another for calculating X,Y"""

def get_J(theta, w, N, dt, OMEGA_x, OMEGA_y, OMEGA_z, X0, Yt):
    """ Calculate J """
 
    J = sum(Yt @ tools.np_multi_matmul(vector_U(theta_k =theta, wj = w, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y, OMEGA_z = OMEGA_z), axis=1) @ X0) / N
            

    return J[0]


















""" Testing Unit """

if __name__ == "__main__":

    print('Testing Funtion : U \n\
        test case inputs    output =')
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


    
    
    U = get_U(theta_k= intial_theta[0], wj = w[0], dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y ,OMEGA_z = OMEGA_z)
    print('for wj = ', w[0], '\ntheta =', intial_theta[0])
    print(U)
    print('Testing Det(Udag * U) = ', np.linalg.det(np.conjugate(U).T @ U))
    
    print('shape of tesnor_U', vector_U(theta_k =intial_theta, wj = w, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y, OMEGA_z = OMEGA_z).shape)
  
    print()
    print()
    print('testing: J')
    J = get_J(theta = intial_theta, w= w, N= N, dt= dt, OMEGA_x= OMEGA_x, OMEGA_y= OMEGA_y, OMEGA_z= OMEGA_z, X0= X0, Yt= Yt)
    print(J)