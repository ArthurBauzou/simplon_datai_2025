test_string = "mieux vaut ne pas mettre un palindrome"

def inverse_string(string:str) :
    res = ""
    lenght = len(string)
    for i in range(lenght) :
        res += string[lenght-i-1]

    return res

print(inverse_string(test_string))