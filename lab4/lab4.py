import random


def pow(number, modula):
    number_save = number
    for _ in range(modula - 2):
        number = number * number_save % modula
    return number


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def ferma_test(n):

    number = random.randint(2, n - 1)
    if gcd(number, n) != 1:
        return False
    if pow(number, n) != 1:
        return False

    return True


def main():
    
    while True:
        
        print('Проверить число на простоту тестом Ферма - \enter')
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))
        except ValueError:
            value = 1
        
        if value == 1:
            
            n = int(input('\nВведите число, которое требуется проверить на простоту тестом Ферма: '))
            number_of_tests = int(input('Введите количество тестов, которое требуется провести: '))
            

            if all([ferma_test(n) for _ in range(number_of_tests)]):
                print('По совокупности тестов, число является простым\n')
            else:
                print('По совокупности тестов, число не является простым\n')

        if value == 2:
            break


if __name__ == '__main__':
    main()
