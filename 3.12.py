k = int(input())
if 1 <= k <= 4:
    print('квартира находится на первом этаже')
elif 5 <= k <= 8:
    print('квартира находится на втором этаже')
elif 9 <= k <= 12:
    print('квартира находится на третьем этаже')
elif 13 <= k <= 16:
    print('квартира находится на четвертом этаже')
elif 17 <= k <= 20:
    print('квартира находится на пятом этаже')
else:
    print('неверно введен номер квартиры')
