num = int(input())
pow = int(input())

answer = 1
if pow > 0:
    for i in range(pow):
        answer *= num
elif pow < 0:
    for i in range(- pow):
        answer /= num

print(answer)