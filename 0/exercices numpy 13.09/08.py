import numpy as np

# version nulle
def one_zero_array(arr) :
    res = []
    for n in arr : res.append(1) if n>5 else res.append(0)
    return res

#version mieux
def is_five_plus(arr) :
    condition = arr >= 5
    return np.where(condition, 1, 0)

test_array = np.array([x for x in np.arange(11)])
print(is_five_plus(test_array))
