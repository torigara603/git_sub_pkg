import numpy as np

def get_square(num:int) -> np.ndarray:
    """ create zero array

    Args:
        num (int): shape

    Returns:
        np.ndarray: zero squeare array
    """
    return np.zeros((num, num))

def get_square_ones(num:int) -> np.ndarray:
    return np.ones((num, num))