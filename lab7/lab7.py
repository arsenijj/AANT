import random

def representation(p):

    twos = 0
    
    while not p % 2:
        twos += 1
        p //= 2
    
    return twos, p


def modula_pow(number, power, modula):

    number_save = number
    
    for _ in range(power - 1):
        number = number * number_save % modula
    return number


def miller_rabin_test(n, k):
    
    s, t = representation(n - 1)
    
    for _ in range(k):
    
        a = random.randint(2, n - 2)
    
        x = modula_pow(a, t, n)
    
        if x == 1 or x == n - 1:
            continue
    
        flag = False
        for _ in range(s - 1):
    
            x = x * x % n
    
            if x == 1:
                return False

            if x == n - 1:
                flag = True
                break
    
        if flag:
            continue
    
        return False
    
    return True


def main():

    while True:
        
        print('\nПроверить число на простоту тестом Миллера-Рабина - \enter')
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))
            
        except ValueError:
            value = 1
        
        if value == 1:

            n = int(input("\nВведите число n: "))
            k = int(input("Введите количество раундов теста: "))
            
            if (miller_rabin_test(n, k)):
                print(f'Число {n} является простым с вероятностью {1 - (1 / 4) ** k}.')
            else:
                print(f'Число {n} не является простым.')

        elif value == 2:
            print('Работа программы завершена')
            return


if __name__ == "__main__":
    main()
   
    # numbers = [i for i in range(17, int(1e4)) if miller_rabin_test(i, 3)]
    # print(numbers)



