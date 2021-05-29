import math
a = int(input())

if a > 1:
    print(math.ceil(math.log2(a)))
elif a == 1:
    print(1)
elif a == 0:
    print(0)