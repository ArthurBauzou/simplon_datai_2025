test_string = "mieux vaut ne pas mettre un palindrome"
pal_string = "Ésope reste ici et se repose"

def normalize(string:str) :
    replace_accents = {
        'e': ['é', 'è', 'ê'],
        'a': ['à', 'â']
    }

    res = string.lower()
    res = res.replace(' ', '')
    for letter, accents in replace_accents.items() :
        for accent in accents :
            res = res.replace(accent, letter)

    return res

def test_pal(string:str) :
    reverse_str = string[::-1]
    reverse_str = normalize(reverse_str)
    string = normalize(string)

    if reverse_str == string :
        return True
    else :
        return False

def test(s) :
    if test_pal(s) :
        print(f"« {s} » est un palindrome")
    else :
        print(f"« {s} » n’est pas un palindrome")

test(test_string)
test(pal_string)