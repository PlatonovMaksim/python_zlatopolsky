abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
if abc**2 == a**3 + b**3 + c**3:
    print('квадрат заданного числа равен сумме кубов его цифр')
else:
    print('не равен')
