abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
if c == 6 or b == 6 or a == 6:
    print ('цифра 6 входит в число')
else:
    print ('цифра 6 не входит в число')
