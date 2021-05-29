import random

print('{Приветственное сообщение от игры}')
while True:
    randomNum = random.randint(1, 100)
    for i in range(5):
        a = int(input('Введите целое число: '))
        if a < randomNum:
            print('Загаданное число больше чем', a)
        elif a > randomNum:
            print('Загаданное число меньше чем', a)
        else:
            print('Поздравляю! Вы угадали')
            break
        if i == 4:
            print('Вы проиграли. Было загадано:', randomNum)
    next = int(input('Хотите начать сначала? (1 - ДА ): '))
    if next != 1:
        break