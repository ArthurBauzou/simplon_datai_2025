import numpy as np

# version nulle
def one_zero_array(arr):
    res = []
    for n in arr : res.append(1) if n>5 else res.append(0)
    return res

#version mieux
def is_five_plus(arr):
    condition = arr >= 5
    print(condition + 3)
    return np.where(condition, 1, 0)

# version avec greater
def greater_than_five(arr):
    return np.greater(arr,5)

test_array = np.array([x for x in np.arange(11)])
print(is_five_plus(test_array))

# print(greater_than_five(test_array))
