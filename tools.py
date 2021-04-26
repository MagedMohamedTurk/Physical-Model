


import numpy as np 
import functools





def np_multi_matmul(tensor: np.ndarray, axis: int) -> np.ndarray:
    arrays = np.split(tensor, tensor.shape[axis], axis = axis)
    multi_mat = functools.reduce(lambda x, y: np.matmul(y, x), arrays)
    
    return multi_mat






def get_w(B, N):

    """ Get j unique random values for w over Bandwidth [-B, B]
    
    """
    w = np.random.uniform(-B,B,[N,1])
    
    return w


def convert_numpy(array, dtype = 'float64'):
    """ Convert arrays into numpy matrix
    float64 type by default """

    dtype_ = np.dtype(dtype)
    return np.array(array, dtype= dtype_)










""" Testing Unit """

if __name__ == "__main__":

    print('Testing Funtion : get_w() \n\
        input (B=3, N=300)   output =', get_w(3,300))