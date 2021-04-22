import numpy as np 
from scipy.linalg import expm
def get_U(theta_k, wj, dt, OMEGA_x, OMEGA_y,OMEGA_z, dtype = 'float64'):
    """ Calculate U
    theta_k = theta element
    wj = w element
    dt = time interval
    OMEGA_x, OMEGA_y, OMEGA_z = ..................... """
    dtype_ = np.dtype(dtype)
    U = np.zeros((3,3), dtype=dtype_)
    
    
    U = expm(dt * ( wj * OMEGA_z +
                            np.cos(theta_k) * OMEGA_x +
                            np.sin(theta_k) * OMEGA_y
                            )
                    )

    return U



def get_J(theta, w, N, dt, OMEGA_x, OMEGA_y, OMEGA_z, X0, Yt):
    """ Calculate J """

    J = 0
   
    for wj in w:
        J_wj = Yt
        for theta_k in theta:
            J_wj = J_wj @ get_U(theta_k =theta_k, wj = wj, dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y, OMEGA_z = OMEGA_z)
        J_wj = J_wj @ X0.T
        J += J_wj
    J = J/N        

    return J



















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
    print(U)
    print()
    print('for wj = ', w[0], '\ntheta =', intial_theta[0])


    print()
    print()
    print('testing: J')
    J = get_J(theta = intial_theta, w= w, N= N, dt= dt, OMEGA_x= OMEGA_x, OMEGA_y= OMEGA_y, OMEGA_z= OMEGA_z, X0= X0, Yt= Yt)
    print(J)
