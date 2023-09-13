number_list = []
verbose = [
    "premier",
    "second",
    "troisième",
    "quatrième",
]
res = []
for i in range(5) :
    valid = False
    while not valid :
        if i < 4 :  number = input(f"entrez un {verbose[i]} nombre entier : ")
        else :      number = input("enfin, entrez le dernier nombre entier : ")

        try :
            number = int(number)
            valid = True
            res.append(number)
        except : 
            print("non, ça n’est pas un nombre entier")

print(res)

