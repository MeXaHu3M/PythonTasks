print("Обмен значениями с промежуточной переменной")
a = int(input())
b = int(input())
c = a
a = b
b = c
print("A =", a, "B =", b)
print("Обмен значениями без промежуточной переменной")
a = int(input())
b = int(input())
a = a + b
b = a - b
a = a - b
print("A =", a, "B =", b)