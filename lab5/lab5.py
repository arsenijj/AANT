import random
import math

def modula_pow(number, modula):
    number_save = number
    for _ in range(modula - 2):
        number = number * number_save % modula
    return number


def is_real_prime(number):
    for i in range(3, number - 1, 2):
        if not number % i:
            return False
    return True
            

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    

def ferma_test(n):
    
    number = random.randint(2, n - 1)
    if gcd(number, n) != 1:
        return False
    elif modula_pow(number, n) != 1:
        return False

    return True


def check_prime():

    n = int(input('\nВведите число, которое требуется проверить на простоту: '))

    if not ferma_test(n):
        print(f'Число {n} не является простым по тесту на основе малой теоремы Ферма')
    else:
        print(f'Число {n} является простым по тесту на основе малой теоремы' \
            ' Ферма, поэтому требуется проверить, не является ли оно числом Кармайкла')

        if not is_real_prime(n):
            print(f'Число {n} не является простым')
        else:
             print(f'Число {n} действительно является простым')
    return

def main():
   
   while True:
        
        print('\nПроверить число на простоту тестом Ферма, а также по свойствам чисел Кармайкла - \enter')
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))
        except ValueError:
            value = 1
        
        if value == 1:
            check_prime()
        elif value == 2:
            print('Работа программы завершена')
            return

if __name__ == '__main__':
    main()
