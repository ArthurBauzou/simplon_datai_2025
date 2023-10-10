test_string = "ceci est une phrase avec des mots (onze, pour être précis)"

def capitalize_words(sentence:str) :
    res = sentence.upper()

    return res

print(capitalize_words(test_string))