import numpy as np

# liste = np.array([[1,2,3],[4,5,6]])
liste = np.array([0,1,2,3,50,3,2,1,0])
print(liste)
# signal = np.random.randn(1000)

def calculator(arr):
    fonctions = {
        "moyenne" : np.mean, 
        "médiane" : np.median, 
        "écart-type" : np.std
        }
    res = {}

    for name, function in fonctions.items() :
        res[name] = function(arr)

    return res

print(calculator(liste))
print("–––")
# print(calculator(signal))