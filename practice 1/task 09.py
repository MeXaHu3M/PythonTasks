firstTime = input().split(':')
h1 = int(firstTime[0])
m1 = int(firstTime[1])

secondTime = input().split(':')
h2 = int(secondTime[0])
m2 = int(secondTime[1])

absM1 = h1 * 60 + m1
absM2 = h2 * 60 + m2

diff = absM1 - absM2

if diff <= 15 and diff >= -15:
    print('Встреча состоится')
else:
    print('Встреча не состоится')
