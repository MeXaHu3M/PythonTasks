numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
colors =  ('g','r','b','r','b','r','b','r','b','r','b','b','r','b','r','b','r','b','r','r','b','r','b','r','b','r','b','r','b','b','r','b','r','b','r','b','r')

red = 0
black = 0

while True:
    num = int(input())
    if num < 0:
        break
    if num < 37:
        numbers[num] += 1
        if colors[num] == 1:
            red += 1
        elif colors[num] == 2:
            black += 1

    for i in range(37):
        if numbers[i] > 0:
            print(i,end=' ')
    print()
    for i in range(37):
        if numbers[i] == 0:
            print(i,end=' ')
    print()
    print(red, black)
    print()