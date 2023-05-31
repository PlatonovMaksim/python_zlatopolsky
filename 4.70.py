k = int(input())
1 <= k <= 365
if (k - 1) % 7 < 5:
    print('рабочий день')
else:
    print('выходной')
