import numpy as np

test_list = [1,2,3,4,5,6,7,8,9]
test_vec = np.array([1,2,3,4,5,6,1,2,3,1])

def no_duplicate(arr:np.array) -> np.array :
    res = np.unique(arr, return_counts=True)

    return res

print(no_duplicate(test_vec))