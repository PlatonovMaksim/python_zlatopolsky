n = int(input())
ed = n % 10
d = n // 10
if n > 9:
    print('число десятков', d, 'число единиц', ed)
else:
    print('неверный формат числа')
