import numpy as np

vectest_1 = np.array([3,5])
vectest_2 = np.array([-8,2])

def produit_scalaire(vec1:np.array, vec2:np.array) -> float :
    res = np.dot(vec1, vec2)

    return res

print(produit_scalaire(vectest_1, vectest_2))


