abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
if a == c:
    print('число является палиндромом')
else:
    print('число не является палиндромом')
