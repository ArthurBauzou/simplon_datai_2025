import random

def randomname() :
    first_names = [
        "pascal",
        "paul",
        "violette",
        "claude",
        "cheryl",
        "tony",
        "hedwige",
        "terry"
    ]
    last_names = [
        "charpentier",
        "swift",
        "wick",
        "mclane",
        "bertignac",
        "parker",
        "tsonga",
        "lee"
    ]
    new_first_name = random.choice(first_names)
    new_last_name = random.choice(last_names)
    return new_first_name + " " + new_last_name

def majusculator(str) :
    words = str.split(' ')
    capitalised_name = ""
    for word in words:
        capital_letter = word[0].upper()
        rest = word.split(word[0],1)[1]
        capitalised_name += capital_letter + rest + ' '

    return capitalised_name

print(majusculator(randomname()))

# print(randomname())