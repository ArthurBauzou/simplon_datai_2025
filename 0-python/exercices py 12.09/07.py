num_list = [n for n in range(100) if n%3 == 0 ]

def sum_of(number_list:list[int]) :
    res = 0
    for n in number_list :
        res += n

    return res

print(sum_of(num_list))