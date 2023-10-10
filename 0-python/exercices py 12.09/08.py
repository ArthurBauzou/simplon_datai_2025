test_list = [
    "poire",
    "cochon",
    "ananas",
    "Gâteau",
    "Ardoise",
    "Oursin",
    "Écran",
    "ukulele",
    "tupperware",
    "oiseau",
    "macaron",
    "œuf",
    "Âtre"
]

def list_of_len(word_list:list[str]) :
    res = [len(w) for w in word_list]
    return res

print(list_of_len(test_list))