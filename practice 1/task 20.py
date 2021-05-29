n = int(input())
k = int(input())

alcohols = []

for i in range(k):
    inp = input().split(' ')
    alcohols.append([inp[0], int(inp[1]), int(inp[2])])

for alcohol in alcohols:
    alcohol.append(alcohol[2] / alcohol[1])

toBuy = []
V = 0


def SetAlcohols():
    global n
    minalcohol = ['none', n + 1, 0, 0]
    for alcohol in alcohols:
        if alcohol[3] > minalcohol[3] and alcohol[1] <= n:
            minalcohol = alcohol
    if minalcohol[1] > n:
        return
    count = int(n / minalcohol[1])
    toBuy.append((minalcohol[0], count))
    n -= count * minalcohol[1]

    global V
    V = count * minalcohol[2]
    SetAlcohols()
SetAlcohols()

print()
print(toBuy[0][0], toBuy[0][1])
print(V)
print(n)