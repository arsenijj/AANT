import random
cnt = 30
ls = []
while cnt:
    a = random.randrange(5, 10)
    b = random.randrange(10, 20)
    c = random.randrange(20, 41)
    d = random.randrange(2, 6)
    if a + b + c + d > 55:
        ls.append((a, b, c, d))
        print(cnt)
        cnt -= 1
print(*ls, sep='\n')