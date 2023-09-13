test_list = [
    1,2,4,8,-7,-56,-2,0,96,457,5.8,4/3,-6.66,64
]

def only_pos(num_list:list) :
    index = 0
    res = []
    while index < len(num_list) :
        if num_list[index] > 0 : res.append(num_list[index])
        index += 1

    return res

print(only_pos(test_list))