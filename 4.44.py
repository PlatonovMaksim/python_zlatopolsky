x = int(input())
y = int(input())
if -1 > x:
    print('точка попала в третью область')
elif -1 < x < 5:
    print('точка не попала во вторую область')
else:
    print('точка попала в первую область')
