number = 8

def gen_fibo(index_max:int) :
    fibo = []
    if index_max == 1 : return [0]
    if index_max > 1 :
        fibo = [0,1]
        for i in range(2,number) :
            fibo.append(fibo[i-2] + fibo[i-1])

    return fibo

for n in gen_fibo(number) :
    print(n)

