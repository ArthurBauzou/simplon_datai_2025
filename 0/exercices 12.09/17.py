n = 12

def enumerate_to_n(number:int) :
    index = 0
    while True :
        print(range(number)[index]+1)
        index += 1
        if index == number : break

enumerate_to_n(n)