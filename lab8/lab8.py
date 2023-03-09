import math
import numpy


def factor(p):
   
    d, factors, unique_factors = 2, [], set()
   
    while d*d <= p:
   
        while (p % d) == 0:
            factors.append(d)
            unique_factors.add(d)
            p //= d
   
        d += 1
   
    if p > 1:
       factors.append(p)
       unique_factors.add(p)

    return list(unique_factors), [factors.count(i) for i in unique_factors]


def pascal_triangle(n):
    
    a = [1]
    
    for _ in range(n):
        b = [1]
        b += [a[k] + a[k + 1] for k in range(len(a) - 1)] + [1]
        a = b

    return [[elem, i] for i, elem in enumerate(a)]


def get_phi(p):

    factors, powers = factor(p)
    
    if len(factors) == 1:
        return p - 1
    else:
        res = [factors[i] ** powers[i] - factors[i] ** (powers[i] - 1) for i 
        in range(len(powers))]

        return numpy.prod(res)


def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)
    

def is_power(number):

    if not number % 2:
        return True, 2, 2

    for i in range(3, math.ceil(math.sqrt(number)), 2):
        i_new = i
        counter = 1
        while i_new < number:
            i_new *= i
            counter += 1
            if i_new == number:
                return True, i, counter    
    return False, None, None


def fast_power(a, n):
    return (1 if n == 0
            else fast_power(a * a, n // 2) if n % 2 == 0
            else a * fast_power(a, n - 1))


def find_r(n, n_log):

    right = n_log ** 2

    first_value = 2

    while True:
        
        if (l := gcd(first_value, n)) != 1 and first_value % n:
            return False, l
        
        elems = [n % first_value]
        elem_save = elem = n % first_value
        order = 1

        while True:

            elem = (elem * elem_save) % first_value

            if elem not in elems:
                elems.append(elem)
                order += 1
            else:
                break
        
        if order > right:

            return True, first_value
            
        else:
            first_value += 1
        

def aks(n):

    result, number, power = is_power(n)
            
    if result:
        if number == 2:
            print(f'Число {n} четное, а, значит, не простое')
        else:
            print(f'Число {n} является степенью другого числа '\
                f'({n} = {number} ^ {power})')
        return


    print(f'Число {n} не является степенью какого-либо числа')

    n_log = math.log2(n)

    res, r = find_r(n, n_log)

    if not res :
        print(f'Было найдено не взаимнопростое число {r} с числом {n}')
        return 
    else:
        print(f'В промежутке [3, {r}] чисел не взаимнопростых с {n} '\
            'найдено не было')

    if n <= r:
        print(f'Число {n} является простым, так как r = {r} и {n} \u2A7D {r}')
        return

    pascal = pascal_triangle(n)

    for a in range(1, math.floor(math.sqrt(get_phi(r)) * n_log) + 1):

        current_pascal = [(coef * fast_power(a, pow_a)) % n == 0 for \
            [coef, pow_a] in pascal][1:-1]

        if not all(current_pascal):
            print(f'Число {n} не является простым')
            return

    print(f'Число {n} является простым')



def main():
  
    while True:
        
        print('\nПроверить число на простоту с помощью теста AKS - \enter')
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))
            
        except ValueError:
            value = 1
        
        if value == 1:

            n = int(input('Введите число: '))
            aks(n)

        elif value == 2:
            print('Работа программы завершена')
            return


if __name__ == "__main__":
    main()