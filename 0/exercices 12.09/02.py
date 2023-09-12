test_list = [
    1,2,4,8,-7,-56,-2,0,96,457,5.8,4/3,-6.66
]

def only_pos(number_list:list) :
    res = []
    for number in number_list :
        if number > 0 : res.append(el)

    return res

def only_pos_comp(number_list:list) :
    res = [n for n in number_list if n > 0]
    return res

print(only_pos_comp(test_list))