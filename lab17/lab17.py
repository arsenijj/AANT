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


def pdf(m_coefs_aboba, n_coefs):

    m_coefs = m_coefs_aboba.copy()
    n = len(n_coefs) - 1

    right = len(m_coefs) - len(n_coefs)
    q_coefs = [0] * (right + 1)

    for k in range(right, -1, -1):
        q_coefs[k] = m_coefs[n + k] // n_coefs[n]

        for j in range(n + k - 1, k - 1, -1):
            m_coefs[j] = (m_coefs[j] - q_coefs[k] * n_coefs[j - k])

    return poly_reduction(q_coefs), poly_reduction((m_coefs[0:n]))


def poly_subtraction(p1, p2, modula):

    if len(p2) > len(p1):
         
        p2 = list(map(lambda x: -x, p2))
        for i, coef in enumerate(p1):
            p2[i] += coef
        return poly_reduction([i % modula for i in p2])

    else:
        for i, coef in enumerate(p2):
            p1[i] -= coef
        return poly_reduction([i % modula for i in p1])


def poly_reduction(f):
    i = 0
    f = f[::-1]
    while i < len(f) and f[i] == 0:
        i += 1
    return (f[i:])[::-1]


def poly_multiplication(p1, p2, modula):

    len_p1, len_p2 = len(p1), len(p2)

    result = [0] * (len_p1 + len_p2 - 1)

    for i in range(len_p1):
        for j in range(len_p2):
            result[i + j] += p1[i] * p2[j]
    return poly_reduction([i % modula for i in result])


def get_content(p):

    for i in range(abs(max(p, key=abs)), 0, -1):
        flag = True
        for j in p:
            if j % i:
                flag = False
                break
        if flag:
            if p[-1] < 0:
                return -i
            else:
                 return i


def geap(p_1, p_2):

    p1, p2 = p_1.copy(), p_2.copy()

    p1_content, p2_content = get_content(p1), get_content(p2)

    c = sympy.gcd(p1_content, p2_content)

    remainder = None

    while p2:
    
        p1_content, p2_content = get_content(p1), get_content(p2)

        p1 = [coef // p1_content for coef in p1]
        p2 = [coef // p2_content for coef in p2]

        lc = p2[-1] ** (len(p1) - len(p2) + 1)
        p1 = [i * lc for i in p1]

        p1, p2 = p2, pdf(p1, p2)[1]
        if p2:
            remainder = p2

    if remainder is None:
        return p_2
        
    if len(remainder) == 1:
        return c
    else:
        last_content = get_content(remainder)
        return [c * i // last_content for i in remainder]


def get_derivative(p):
    return [coef * (i + 1) for i, coef in enumerate(p[1::])]


def psqff(p):

    p_derivative = get_derivative(p)
    r = geap(p, p_derivative)
    t = pdf(p, r)[0]
    j = 1
    ls = []

    while len(r) != 1:
        
        v = geap(r, t)
        s = pdf(t, v)[0]
        ls.append(s)
        print(p, r, s, t)
        r = pdf(r, v)[0]
        t = v
        j += 1

    return ls + [t]


def left_bracket():
    print('(', end='')
    return


def main():

    while True:
        
        print('\nВыполнить разложение полинома на свободные от квадратов' + 
        'множители  - \enter')
    
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))

        except ValueError:
            value = 1

        if value == 1:

            p = get_coefs()
            print('Полином имеет вид: ')
            polinomial_view(p)

            brackets = psqff(p[::-1])
            if brackets[0] == [1]:
                brackets = brackets[1::]
                start_value = 2
            else:
                 start_value = 1

            polinomial_view(p, True)
            print(' = ', end='')
            
            for bracket in brackets:
                left_bracket()
                polinomial_view(bracket[::-1], True)
                print(f')^{start_value} * ', end = '')
                start_value += 1
            print('1')

        else:
            print('Работа программы завершена')
            return


if __name__ == "__main__":     
    main()
