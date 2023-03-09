def bezout_recursive(a, b):

    if not b:
        return (1, 0, a)
    y, x, g = bezout_recursive(b, a % b)
    return (x, y - (a // b) * x, g)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


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

            g = gcd(a,m)
            print(f'НОД({a}, {m}) = {g}')

            if not b % g:

                print(f'И {b} делится на {g}. Это означает, что всего решений'\
                    f' сравнения: {g}.')
                
                a //= g
                b //= g
                m_save = m
                m //= g
                
                print(f'Разделим сравнение и его модуль на {g} и получим:'\
                    f' {a} * x \u2261 {b} (mod {m})')

                q, _, _ = bezout_recursive(a, m)        

                x_0 = b * q % m_save
                
                print('Решения сравнения:')
                
                print('x_0 =', x_0)

                for i in range(1, g):
                    print(f'x_{i} = {(x_0 + i * m) % m_save}')

            else:
                print(f'Сравнение не имеет решений, так как {b} не делится на {g}.')


        if value == 2:
            print('Работа программы завершена')
            return


if __name__ == "__main__":
    main()