import random

first_names = [
    "pasclal",
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

def randomname() :
    new_first_name = random.choice(first_names)
    new_last_name = random.choice(last_names)
    return new_first_name + new_last_name


