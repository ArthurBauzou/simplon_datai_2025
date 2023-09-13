import numpy as np

liste = np.arange(0,40,2)
signal = np.random.randn(1000)


def batch_calculator(arr):
    fonctions = {
        "moyenne" : np.mean, 
        "médiane" : np.median, 
        "écart-type" : np.std
        }
    res = {}

    for name, function in fonctions.items() :
        res[name] = function(arr)

    return res

print(batch_calculator(liste))
print("–––")
print(batch_calculator(signal))