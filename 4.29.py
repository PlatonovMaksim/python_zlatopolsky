ab = int(input())
c = int(input())
a = ab // 10
b = ab % 10
if  (a + b) % 3 == 0:
    print('сумма цифр заданного числа кратна трем')
elif  (a + b) % c == 0:
    print('сумма цифр заданного числа кратна', c)
