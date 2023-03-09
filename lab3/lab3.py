def fact(n):
    res = 1
    for i in range(2, n + 1):
        res *= i 
    return res


def vislon_criteria(n):
    return not (fact(n - 1) + 1) % n


def main():
    
    while True:
        
        print('\nПроверить число на простоту критерием Вильсона - \enter')
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))
        except ValueError:
            value = 1
        
        if value == 1:
            
            n = int(input('\nВведите число, которое требуется проверить на простоту: '))
            if vislon_criteria(n):
                print(f'Число {n} является простым.')
            else:
                print(f'Число {n} не является простым.')

        if value == 2:
            print('Работа программы завершена')
            return


if __name__ == '__main__':
    main()
  
