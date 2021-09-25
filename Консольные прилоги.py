# Базовый функционал


from random import randint
o = int(input ())
b = 0
a = randint (1,1000)
while a != o:
    b += 1
    if o > a:
        print (f'Загаданное число меньше, количество попыток: {b}')
    elif o < a:
        print (f'Загаданное число больше, количество попыток: {b}')
    o = int(input ())
print (f'Вы угадали, это число {a} и Вы потратили {b} попыток')



# По модулю 


from random import randint
o = int(input ())
b = 0
a = randint (1,1000)
if a < 0:
    a = abs (a)
else:
    a == a
while a != o:
    b += 1
    if o > a:
        print (f'Загаданное число меньше, количество попыток: {b}')
    elif o < a:
        print (f'Загаданное число больше, количество попыток: {b}')
    o = int(input ())
print (f'Вы угадали, это число {a} и Вы потратили {b} попыток')


# С повтором

from random import randint
o = int(input ())
b = 0
k = []
a = randint (1,1000)
if a < 0:
    a = abs (a)
else:
    a == a
while a != o:
    i = o
    if i not in k:
        k.append (i)
    elif i in k:
        print ('Вы повторяетесь')
        o = int(input ())
        continue
    b += 1
    if o > a:
        print (f'Загаданное число меньше, количество попыток: {b}')
    elif o < a:
        print (f'Загаданное число больше, количество попыток: {b}')
    o = int(input ())
print (f'Вы угадали, это число {a} и Вы потратили {b} попыток')