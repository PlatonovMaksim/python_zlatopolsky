a = int(input())
b = int(input())
c = int(input())
d = b**2 - 4*a*c 
if d > 0:
    print('уравнение имеет два корня')
elif d < 0:
    print('уравнение не имеет корней')
else:
    print('уравнение имеет один корень')
