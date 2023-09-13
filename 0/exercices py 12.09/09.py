num_list = [n for n in range(30) if n%3 == 0 ]

def only_even(numlist:list) :
    res = [n for n in numlist if n%2 == 0 ]
    return res

print(only_even(num_list))