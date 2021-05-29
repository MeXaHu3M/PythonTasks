import math

a = float(input())
b = float(input())
c = float(input())

D = b * b - 4 * a * c

if a != 0:
    if D > 0:
        print('x1 =', (-b + math.sqrt(D)) / (2 * a))
        print('x2 =', (-b - math.sqrt(D)) / (2 * a))
    elif D == 0:
        print('x =', -b / (2 * a))
    else:
        print('\nКорней нет')
else:
    print('x =', -c / b)