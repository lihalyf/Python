import numpy as np

def fibo_list(s):
    list_a = []
    for times in range(s):
        b = fibo(times)
        list_a.append(b)
    print(list_a)
    
def fibo(i):
    if i == 0:
        return 1
    elif i ==1:
        return 1
    else:
        return fibo(i-1) + fibo(i-2)

fibo_list(8)


def dp_fibo_list(m):
    list_b = np.zeros(m)
    list_b[0] = 1
    list_b[1] = 1
    for i in range(2, m):
        list_b[i] = list_b[i-1] + list_b[i-2]
    print(list_b)
    
dp_fibo_list(1000)