x = int(input())
y = int(input())
if x > 0 or y > 0:
    print('точка находится во второй области')
elif x < 0 or y > 0:
    print('точка находится в первой области')
