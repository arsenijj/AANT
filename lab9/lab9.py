import random

def sieve_of_eratosthenes(n):
    sieve = list(range(2,n))
    i = 0
    while True:
        cur_elem = sieve[i]
        cur_elem_in_power = cur_elem ** 2
        if cur_elem_in_power <= n:
            start_position = min(filter(lambda x : x >= cur_elem_in_power, sieve))
            for elem in sieve[sieve.index(start_position):]:
                if not elem % cur_elem:
                    sieve.remove(elem)
            i += 1

        else:
            return sieve

def power(a, n):
    return (1 if n == 0
            else power(a * a, n // 2) if n % 2 == 0
            else a * power(a, n - 1))


def lucas_lehmer_test(p):
    s = 4
    k = 1
    m = power(2, p) - 1
    while k != p - 1:
        s = (s * s - 2) % m
        k += 1
    return m if not s else False


def main():
    exists = []
    while True:
        
        print('\nПостроить большое простое число с помощью Критерия Люка - \enter')
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))
            
        except ValueError:
            value = 1
        
        if value == 1:
            while True:
                p = sieve_of_eratosthenes(2000)
                a = p[random.randrange(0, len(p))]
                if a not in exists:
                    exists.append(a)

                    m = lucas_lehmer_test(a)
                    if m:
                        print(f'Случайно было выбрано простое число p = {a}')
                        print(f'Построено простое число: {m}')
                        break
            

        elif value == 2:
            print('Работа программы завершена')
            return


if __name__ == "__main__":
    main()