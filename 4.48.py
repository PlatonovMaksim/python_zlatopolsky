a = int(input())
b = int(input())
if a % b == 0:
    print(b, 'является делителем числа', a)
elif b % a == 0:
    print(a, 'является делителем числа', b)
else:
    print('число не является делителем')
