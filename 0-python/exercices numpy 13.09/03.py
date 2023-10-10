import numpy as np

tabl = np.array([1, 3, 5, 7, 9])

def my_sum(arr:np.array) -> int :
    return np.sum(tabl)

print(my_sum(tabl))