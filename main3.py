# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 0
while count < 10:
    x = int(input('Введите число: '))
    if num > x:
        print('Загаданное число больше')
    elif num < x:
        print('Загаданное число меньше')
    else:
        print('Правильно')
    count += 1

