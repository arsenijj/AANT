import sympy

def polinomial_view(coefs, flag=False):
    n = len(coefs) - 1
    a = ''
    mul = '*'
    if coefs:

        last = coefs[-1]
        coefs = coefs[:-1:]
        if coefs:
            for i, coef in enumerate(coefs):
                if coef:
                    print(f'{str(coef) + mul if coef != 1 else a}x^{n - i} +', end=' ')
        print(last, end='')
    else:
        print(coefs, end='')
    if not flag:
        print()
    return


def get_field():
    n = int(input('Введите поле, в котором требуется поделить многочлены: '))
    if not sympy.isprime(n):
        print('Вы ввели не простое число')
        return get_field()
    else:
        return n
    

def get_coefs(j=None):
    print('Введите коэффициенты полинома, начиная с коэффициента при' +
    ' наибольшей степени:')
    koef_modula = lambda x : int(x) % j
    koef_integer = lambda x : int(x)
    coefs = map(koef_modula if j is not None else koef_integer, input().split())
    return list(coefs)


def gcdExtended(a, b):
    if a == 0 :
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def divide_in_modula(a, b, j):
    _, x, _ = gcdExtended(b, j)
    b_inversed = ((x % j + j) % j)
    return (a * b_inversed) % j


def pdf(m_coefs, n_coefs, p, flag=False):

    m = len(m_coefs) - 1
    n = len(n_coefs) - 1

    right = len(m_coefs) - len(n_coefs)
    q_coefs = [0] * (right + 1)

    for k in range(right, -1, -1):
        
        if not flag:
            q_coefs[k] = divide_in_modula(m_coefs[n + k], n_coefs[n], p)
        else:
            q_coefs[k] = m_coefs[n + k] // n_coefs[n]

        for j in range(n + k - 1, k - 1, -1):
            m_coefs[j] = (m_coefs[j] - q_coefs[k] * n_coefs[j - k])
            if not flag:
                m_coefs[j] %= p
        
    return q_coefs[::-1], (m_coefs[0:n])[::-1]


def main():

    while True:
        
        print('\nВыполнить полиномиальное деление PDF - \enter')
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))

        except ValueError:
            value = 1
        
        if value == 1:
            
            print('Деление в поле простого числа - 1, деление в поле целых чисел - 2')
            division_option = int(input())
            j = None

            if division_option == 1:
                j = get_field()
                m_coefs_save = m_coefs = get_coefs(j)
                print(f'Введите от 0 до {len(m_coefs)} коэффициентов')
                n_coefs = get_coefs(j)
            else:
                m_coefs_save = m_coefs = get_coefs()
                print(f'Введите от 0 до {len(m_coefs)} коэффициентов')
                n_coefs = get_coefs()
                
            print('Полином 1 имеет вид:')
            polinomial_view(m_coefs)
            
            print('Полином 2 имеет вид')
            polinomial_view(n_coefs)
            if division_option == 1:
                q, r = pdf(m_coefs[::-1], n_coefs[::-1], j)
            else:
                q, r = pdf(m_coefs[::-1], n_coefs[::-1], j, True)
            print(q, r)
            print('(', end='')
            polinomial_view(m_coefs_save, flag=True)
   
            print(')', end='')

            print(' \\ (', end='')
            polinomial_view(n_coefs, flag=True)
            print(') = ', end='')

            print('(', end='')
            polinomial_view(n_coefs, flag=True)
           
            print(') * ', end='')

            print('(', end='')
            polinomial_view(q, flag=True)
            print(') + ', end='')

            print('(', end='')
            polinomial_view(r, flag=True)
            print(')')

        elif value == 2:
            print('Работа программы завершена')
            return


if __name__ == "__main__": 
    main()
