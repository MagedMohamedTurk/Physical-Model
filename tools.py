

import random 
import numpy as np 

def get_w(B, j):

    """ Get j unique random values for w over Bandwidth [-B, B]
    
    """

    
    return np.random.uniform(-B,B,[j,1])


def convert_numpy(array, dtype = 'float64'):
    """ Convert arrays into numpy matrix
    float64 type by default """

    dtype_ = np.dtype(dtype)
    return np.array(array, dtype= dtype_)










""" Testing Unit """

if __name__ == "__main__":

    print('Testing Funtion : get_w() \n\
        input (B=3, j=10)   output =', get_w(3,20))