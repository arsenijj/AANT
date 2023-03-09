import numpy


def pow(number, modula, power):
    number_save = number
    for _ in range(power - 2):
        number = number * number_save % modula
    return number


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)



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


def get_phi(p):

    factors, powers = factor(p)
    
    if len(factors) == 1:
        return p - 1
    else:
        res = [factors[i] ** powers[i] - factors[i] ** (powers[i] - 1) for i 
        in range(len(powers))]

        return numpy.prod(res)


def main():
    
    while True:
        
        print('\nВвести числа a, b, m - \enter')
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))
        except ValueError:
            value = 1
        
        if value == 1:
            
            a = int(input('Введите значение a: '))
            b = int(input('Введите значение b: '))
            m = int(input('Введите значение m: '))
            a %= m
            b %= m

            print(f'\nСравнение имеет вид {a} * x \u2261 {b} (mod {m})')

            d = gcd(a, m)
            print(f'НОД({a}, {m}) = {d}')
            
            if not b % d:
                print(f'И {b} делится на {d}. Это означает, что количество решений составляет {d}')
                
                a //= d
                b //= d
                m_save = m
                m //= d
                print(f'Разделим сравнение и его модуль на {d} и получим: {a} * x \u2261 {b} (mod {m})')

                

            else:
                print(f'Сравнение не имеет решений, так как {b} не делится на {d}.')


        if value == 2:
            print('Работа программы завершена')
            return


if __name__ == "__main__":
    lst = [16, 24, 24, 16, 'ab', 'ab', 32, 36, 32, 24, 'ab', 44]
    
    print(lst)
    ls = []
    for i in lst:
        if i == 'ab':
            ls.append('ab')
            continue
        # print(get_phi(i), end=', ')
        ls.append(get_phi(i))
    print(ls)
    # main()
