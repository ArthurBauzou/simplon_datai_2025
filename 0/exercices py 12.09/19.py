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
    "Macaron",
    "œuf",
    "Âtre"
]

def only_vowel(word_list:list):
    index = 0
    res = []
    vowels = ("a","e","i","o","u","y","à","é","è","ê","œ","ï","â")
    while index < len(word_list) :
        if word_list[index][0].lower() in vowels : res.append(word_list[index])
        index += 1

    return res

print(only_vowel(test_list))