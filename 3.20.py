abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
s = a + b + c
p = a*b*c
print('число единиц', c)
print('число десятков', b)
print('сумма его цифр', s)
print('произведение его цифр', p)
