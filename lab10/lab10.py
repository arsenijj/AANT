from sympy import *
import random


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


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


def pocklington_criterion(n):

    limit = 10 ** n

    primes = list(primerange(10000))
    
    s = random.choice(primes)
    print(f'Случайно было выбрано простое число {s}\n')

    right = 2 * (2 * s + 1)

    while s < limit:
        print(f'\nНа текущем шаге значение s = {s}')

        while True:

            r = random.randrange(s + 1, right, 2)
            # print(f'Случайно было выбрано четное число {r}') #\u2208 [{s}, {right}]\n')

            n = s * r + 1
            # print(f'На простоту проверяется число {n}\n')

            flag = False
            for prime in primes:
                if not n % prime:
                    flag = True
                    # print(f'Число оказалось не простым, так как имееет '\
                        # f'делитель ({prime})\n')
                    break

            if flag:
                continue

            while True:
 
                a = random.randint(2, n - 1)
                # print(f'Случайно было выбрано число {a}') #\u2608 [{2}, {n - 1}]\n')

                if modula_power(a, n - 1, n) != 1:
                    # print(f'Число {n} оказалось непростым, так как '\
                    #     f'{a} ^ {n - 1} \u2241 1 (mod {n})\n')
                    break
                else:
                    pass
                    #  print(f'{a} ^ {n - 1} \u2263 1 (mod {n})\n')

                d = gcd((modula_power(a, r, n) - 1), n)
 
                if d != n:
                    if d == 1:
                        # print(f'Переход к следующей итерации алгоритма \n') 
                        s = n
                        right = 2 * (2 * s + 1)
                        break 
                    else: 
                        continue
                else: 
                    continue

            if s == n:
                 break
    return s


def main():

    while True:
        
        print('\nПостроить большое простое число с помощью критерия Поклингтона - \enter')

        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))
            
        except ValueError:
            value = 1
        
        if value == 1:
            n = int(input('Введите порядок числа, которое будет строится: '))
            generated_prime = pocklington_criterion(n)
            print(f'Было получено простое число {generated_prime}')
            
        elif value == 2:
            print('Работа программы завершена')
            return


# if __name__ == "__main__":
#     main()

print(isprime(838434946436548634993304532759154926858853757855388198078658510013590060003281425337004337205082084057227549480245471337944085694264304790150508367904537753328882651210314542140401732162069741553608285313318797286876880246301092522682515482451837716128847860936271))