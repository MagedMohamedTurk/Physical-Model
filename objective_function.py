import numpy as np 
def get_U(theta_k, wj, dt, OMEGA_x, OMEGA_y,OMEGA_z, dtype = 'float64'):
    """ Calculate U
    theta_k = theta element
    wj = w element
    dt = time interval
    OMEGA_x, OMEGA_y, OMEGA_z = ..................... """
    dtype_ = np.dtype(dtype)
    U = np.zeros((3,3), dtype=dtype_)
    
    
    U = np.exp(dt * ( wj * OMEGA_z +
                            np.cos(theta_k) * OMEGA_x +
                            np.sin(theta_k) * OMEGA_y
                            )
                    )

    return U



def get_J(theta, w, N, dt, OMEGA_x, OMEGA_y, OMEGA_z, X0, Yt):
    """ Calculate J """

    J = 0
   
    for _, wj in enumerate(w):
        J_wj = Yt
        for theta_k in theta:
            J_wj = J_wj @ get_U(theta_k, wj, dt, OMEGA_x, OMEGA_y, OMEGA_z)
        J_wj = J_wj @ X0.T
        J += J_wj
    J = (1/N) * J         

    return J



















""" Testing Unit """

if __name__ == "__main__":

    print('Testing Funtion : U \n\
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


    
    U = get_U(theta_k= intial_theta[0], wj = w[0], dt = dt, OMEGA_x = OMEGA_x, OMEGA_y = OMEGA_y ,OMEGA_z = OMEGA_z)
    print(U)


    print()
    print()
    print('testing: J')
    J = get_J(theta = intial_theta, w= w, N= N, dt= dt, OMEGA_x= OMEGA_x, OMEGA_y= OMEGA_y, OMEGA_z= OMEGA_z, X0= X0, Yt= Yt)
    print(J)
