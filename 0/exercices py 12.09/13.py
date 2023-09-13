test_string = "ceci est une phrase avec des mots (onze, pour être précis)"

def count_words(sentence:str) :
    res = len(sentence.split())

    return res

print(count_words(test_string))