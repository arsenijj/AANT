from sympy import *
import math 
import random
import numpy as np
from numpy import sum as npsum
from itertools import chain, combinations



def combs(matr):
    arr = []
    for k in range(2, len(matr) + 1):
        rows = combinations(matr,k)
        indices = list(combinations(range(len(matr)), k))
        for i, j in enumerate(rows):
            if sum(npsum(j, axis=0) % 2) == 0: 
                arr.append(indices[i])
    return min(arr, key=len)


def base_smoothness(a, base):

    vector = [0] * len(base)

    for i, divider in enumerate(base):
        while not a % divider:
            a //= divider
            vector[i] += 1

    if a == 1:
        return True, vector, [elem % 2 for elem in vector]
    else:
        return False, None, None


def dixon_factorization(n):

    l = math.exp(math.sqrt(math.log(n) * math.log(math.log(n))))
    print('L =', l)

    m = l ** (1 / 2) * 4
    print('M =', m)

    factor_base = list(sieve.primerange(m + 1))
    print('Фактор-база B = {', *factor_base, '}')

    a_vectors = []
    e_vectors = []
    b_i = []

    h = len(factor_base)

    left = math.floor(math.sqrt(n)) + 1
    right = n - 1

    while len(a_vectors) - 1 != h:

        b = random.randint(left, right)

        a = (b * b) % n
        if a == 0:
            continue

        is_smooth, a_vector, e_vector = base_smoothness(a, factor_base)

        if is_smooth and b not in b_i: 
        # and any(e_vector):
            a_vectors.append(a_vector)
            e_vectors.append(e_vector)
            b_i.append(b)


    print('\nb_i', b_i)
    print('\na_i:', *a_vectors, sep='\n')
    print('\ne_i:', *e_vectors, '\n', sep='\n')
  

    lin_res = combs(e_vectors)

    if len(lin_res) == 0:
        return False  
    else:
        print(f'Номера линейно зависимых векторов в матрице e_i: {lin_res} ')

    x = np.prod([b_i[number] for number in lin_res]) % n

    powers_list = [0] * len(factor_base)
    for i in lin_res:
        for number, power in enumerate(a_vectors[i]):
            powers_list[number] += power

    y = prod([factor_base[i] ** (elem // 2) for i, elem in \
        enumerate(powers_list)]) % n
    

    if y != x and x != (n - y):
        u = gcd(n, x - y)
        v = gcd(n, x + y)
        if u * v != n:
            return False
        else:
            print(f'{u} * {v} = {n}')
            return True
    else:
        return False
        

def main():

    while True:
        
        print('\nВыполнить факторизацию методом Диксона - \enter')
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))
            
        except ValueError:
            value = 1
        
        if value == 1:

            n = int(input('Введите число, которое требуется факторизовать: '))
            if isprime(n):
                print('Вы ввели простое число')
            fl = False
            while not fl:
                fl = dixon_factorization(n)

            # dixon_factorization(n)

        elif value == 2:
            print('Работа программы завершена')
            return


if __name__ == "__main__": 
    main()
    
    # print(divisors(43498))
    # res = []
    # for i in range(1, 21749):
    #     for j in range(1, 21750):
    #         if (i + j) * (i - j) == 43498:
    #             res.append((i, j))
    #     print(i)
    # print(res)