import random

def gcd(a, n):

    if a == 0:
        return n
    else:
         return gcd(n % a, a)


def modula_power(a, power, modula):
    
    b = 1
    while power:
        if not power % 2:
            power //= 2
            a = (a * a) % modula
        else:
            power -= 1
            b = (b * a) % modula
    return b


def get_jacobi(a, n, res):
    
    if a == 0:
        return res

    twos = 0
    while not a % 2:
        a //= 2
        twos += 1
    
    if twos % 2:
        res *= -1 if ((n * n - 1) // 8) % 2 else 1


    res *=  -1 if ((a - 1) * (n - 1) // 4) % 2 else 1

    return get_jacobi(n % a, a, res)


def solovay_shtrassen_test(n, k):

    if not n % 2:
        return [], [2]

    power = (n - 1) // 2
    witnesses_of_simplicity = []
    witnesses_of_not_simplicity = []

    for _ in range(k):

        a = random.randrange(2, n - 1)
        if gcd(a, n) != 1:
            witnesses_of_not_simplicity.append(a)
        else:
            if modula_power(a, power, n) == get_jacobi(a, n, 1) % n:
                witnesses_of_simplicity.append(a)
            else:
                witnesses_of_not_simplicity.append(a)

    return witnesses_of_simplicity, witnesses_of_not_simplicity        


def main():
    
    while True:
        
        print('\nПроверить число на простоту тестом Соловея-Штрассена - \enter')
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))
        except ValueError:
            value = 1
        
        if value == 1:
            
            n = int(input('\nВведите число, которое требуется проверить на '\
                'простоту тестом Соловея-Штрассена: '))

            number_of_tests = int(input('Введите количество тестов, которое '\
                'требуется провести: '))
            
            witnesses_of_simplicity, witnesses_of_not_simplicity = solovay_shtrassen_test(n, number_of_tests)

            if not witnesses_of_not_simplicity:
                
                print(f'Число {n} является простым с вероятностью {1 - (1/4)**number_of_tests}')
                print(f'Свидетелями его простоты являются числа {witnesses_of_simplicity}')
            
            else:
                
                print(f'Число {n} не является простым')
                print(f'Свидетелями его непростоты являются числа {witnesses_of_not_simplicity}')
                
                if witnesses_of_simplicity:
                    print(f'Лжесвидетелями его простоты являются числа {witnesses_of_simplicity}')

        if value == 2:
            break


if __name__ == '__main__':
    main()
