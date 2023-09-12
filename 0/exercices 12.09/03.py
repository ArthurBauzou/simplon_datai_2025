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

def only_vowel(word_list:list):
    res = []
    vowels = ("a","e","i","o","u","à","é","è","ê","œ","ï","â")
    for word in word_list :
        if word[0].lower() in vowels : res.append(word)

    return res

print(only_vowel(test_list))
