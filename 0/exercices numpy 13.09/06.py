import numpy as np

test_array = np.array([x for x in np.arange(1,48,2.5)])
np.random.shuffle(test_array)

def remettre_en_ordre(arr) :
    res = np.sort(arr)
    return res

print(f"la table toute emmêlée 😫 : {test_array}")
print(f"la table bien ordonée 🤗 : {remettre_en_ordre(test_array)}")

