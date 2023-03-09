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


def get_coefs():
    print('Введите коэффициенты полинома, начиная с коэффициента при' +
    ' наибольшей степени:')
    koef_integer = lambda x : int(x)
    coefs = map(koef_integer, input().split())
    return list(coefs)


def divide(number, coefs):
    new_coefs = [coefs[0]]
    cur = coefs[0]

    for i in coefs[1::]:
        cur = cur * number + i
        new_coefs.append(cur)
    if not new_coefs[-1]:
        return True, new_coefs[:-1:]
    else:
        return False, coefs


def horner_schema(p : list, dividers : dict):
    
    for i in sympy.divisors(p[-1]):
        result, new_coefs = divide(i, p)            
       
        if result:
            p = new_coefs
            if i not in dividers.keys():
                dividers[i] = 1
            else:
                dividers[i] += 1

            return horner_schema(p, dividers)

        else:
            result1, new_coefs_other = divide(-i, p)
            if result1:
                p = new_coefs_other
                if -i not in dividers.keys():
                    dividers[-i] = 1
                else:
                    dividers[-i] += 1
    
                return horner_schema(p, dividers)

    return p, dividers


def compute_value(poly : dict):
    
    x = int(input('Введите точку, в которой требуется посчитать значение полинома: '))
    result = 1

    for (key, value) in poly.items():
        result *= ((x + key) ** value)
    print(f'Значение полинома в точке {x} равно {result}')
    return


def left_bracket():
    print('(', end='')
    return


def main():

    while True:
        
        print('\nВычислить значения и корни полинома - \enter')
        
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))

        except ValueError:
            value = 1
        
        if value == 1:
            
            p = get_coefs()
            
            poly, result = horner_schema(p.copy(), dict())
            print('Полином имеет вид: ')
            polinomial_view(p)
    
            if poly != [1]:
                print('Полином не является приводимым')
            else:
    
                print('Данный полином можно представить ввиде:')
                polinomial_view(p, True)
                print(' = ', end='')

                for (key, value) in result.items():
                    print(f'(x + {key}) ^ {value} * ', end='')
                print(1)

                print(f'Целочисленные значения корней: {result.keys()}')
                
                chosen_option = int(input('Вычислить значение полинома в точке - 1: '))
                if chosen_option == 1:
                    compute_value(result)

        elif value == 2:
            print('Работа программы завершена')
            return


if __name__ == "__main__":    
    main()

# Пример:
# horner_schema([1, 2, -21, -20, 71, 114, 45], dict())