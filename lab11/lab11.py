import math

def factorization(n, res):

    sq = math.ceil(math.sqrt(n))
    k = 0

    while True:

        subres1 = (sq + k) ** 2 - n
        subres = math.sqrt(subres1)

        if not math.ceil(subres) == math.floor(subres):
            k += 1
        else:
            subres = math.ceil(subres)
            break
    
    if len(res) > 0:
        for i, a in enumerate(res):
            if sq + k - subres == a[2] or sq + k + subres == a[2]:
                if a[2] != 1:
                    res.remove(a)
                res.insert(i, [sq + k, subres, sq + k - subres])
                res.insert(i + 1, [sq + k, subres, sq + k + subres])
                break
    else:

        res.append([sq + k, subres, sq + k - subres])
        res.append([sq + k, subres, sq + k + subres])

    if sq + k - subres > 1:
     
            factorization(sq + k - subres, res)

            factorization(sq + k + subres, res)

    return res
   


def main():

    while True:
        
        print('\nВыполнить факторизацию Ферма - \enter')
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))
            
        except ValueError:
            value = 1
        
        if value == 1:

            n = int(input("\nВведите число n: "))
            twos = 0
            n_save = n

            while not n % 2:
                n //= 2
                twos += 1
            
            res= factorization(n, [])

            if twos != 0:
                print(f'{n_save} = {2}^{twos} *', end='')
            else:
                print(f'{n_save} = ', end='')
            
            for (a, b, _) in res[:-1:2]:
                print(f'({a} - {b})({a} + {b})', end='')
            
        elif value == 2:
            print('Работа программы завершена')
            return


if __name__ == "__main__":
    main()