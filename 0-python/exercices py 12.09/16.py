import random

secret_num = random.choice(range(1,1000))
win = False
print("Essayez de deviner à quel entier je pense, entre 1 et 1000 🧙‍♂️ : \n")

n = 0

while not win :
    n += 1
    guess = input(f"Essai n° {n} >>>  ")
    try :
        guess = int(guess)
        if guess > secret_num :
            print("C’est moins ! \n")
        elif guess < secret_num :
            print("C’est plus ! \n")
        else : 
            print("Ouiouiouioui OUIIII !! Vous gagnez une encyclopédie Larousse 🤑 \n")
            win = True
    except : 
        print("non, ça n’est pas un nombre")