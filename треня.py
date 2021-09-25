# Задания по вариантам:
# 1. Написать консольное приложение (Угадай-число)
# Программа при старте загадывает рандомное число от 1 до 1000
# И просит пользователя угадать загаданное число.
# При каждой попытке программа должна вывести номер попытки и результат сравнения с загаданным числом
# (больше, меньше, Угадали)

# Можно добавить:
# 1.1 загадывать как положительные так и отрицательные числа а сравнивать их по модулю
# 1.2 При повторном вводе одного и того же значения, вывести соответсвующее сообщение
# 1.3 Вести таблицу лидеров (для этого надо попросить пользователя ввести имя при начале игры)
# 1.4 Добавить меню (1. Играть 2. Таблицы лидеров 3. Выход)

from random import randint
fl = open('./Results.txt') 
def res (name, b):
    fl = open('./Results.txt', 'a') 
    fl.write(f'{name} had {b} trying \n')
    fl.close()

def one():
    print ('Good, lets go..')
    name = input('Представьтесь пожалуйста ')
    o = int(input ('Предложите Ваше число: '))
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
    print (f'{name}, Вы угадали, это число {a} и Вы потратили {b+1} попыток')
    res (name, b)
    four ()
    
def two ():
    print(fl.read())
    four ()
def three ():
    print('Okay, I"m exiting of the game')
    raise SystemExit
def four ():
    print ('Что делаем дальше?')
    choice = int(input ('Сделайте Ваш выбор пожалуйста: '))
    if choice == 1:
        one()
    elif choice == 2:
        two()
    else:
        three()

print ('The Menu of this game:\n 1. Play\n 2. View the results\n 3. Exit')
choice = int(input ('Сделайте Ваш выбор пожалуйста: '))
if choice == 1:
    one()
elif choice == 2:
    two()
else:
    three()


