num = int(input())

prime = True
i = 2
while prime and i * i < num:
    if num % i == 0:
        prime = False
        break
    i += 1

if prime:
    print('Простое')
else:
    print('Составное')