kmh = int(input())
ms = int(input())
if kmh < ms * 1000/3600:
    print("Скорость в километрах быстрее")
else:
    print("Скорость в метрах быстрее")
