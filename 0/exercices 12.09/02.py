test_list = [
    1,2,4,8,-7,-56,-2,0,96,457,5.8,4/3,-6.66
]

def only_pos(lst:list):
    res = []
    for el in lst :
        if el > 0 : res.append(el)

    return res

print(only_pos(test_list))