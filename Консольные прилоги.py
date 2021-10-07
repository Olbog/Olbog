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


# С меню и таблицей лидеров

from random import randint
fl = open('./Results.txt') 
def res (name, b):
    fl = open('./Results.txt', 'a') 
    fl.write(f'{name} had {b} trying \n')
    fl.close()

print ('The Menu of this game:\n 1. Play\n 2. View the results\n 3. Exit')
choice = int(input ('Сделайте Ваш выбор пожалуйста: '))
if choice == 1:
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
    print (f'{name}, Вы угадали, это число {a} и Вы потратили {b} попыток')
    res (name, b)
elif choice == 2:
    print(fl.read())
else:
    print('Okay, I"m exiting of the game')
    raise SystemExit

    # С меню, таблицей лидеров и непрерывной работой

from random import randint
fl = open('./Results.txt') 
def res (name, b):
    fl = open('./Results.txt', 'a') 
    fl.write(f'{name} had {b} trying \n')
    fl.close()

def zero (x):
    if x == 1:
        one()
    elif x == 2:
        two()
    else:
        three()

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
    zero(choice)

print ('The Menu of this game:\n 1. Play\n 2. View the results\n 3. Exit')
choice = int(input ('Сделайте Ваш выбор пожалуйста: '))
zero(choice)



from random import randint
file_l = open('./Results.txt') 

def print_menu():
    print('Menu: ')
    for k, value in MENU.items():
        print(f'{k} {value.__name__}')


def write_results(name, b):
    file_l = open('./Results.txt', 'a') 
    file_l.write(f'{name} had {b+1} trying \n')
    file_l.close()



def play():
    print('Good, lets go..')
    name = input('Представьтесь пожалуйста ')
    o = int(input('Предложите Ваше число: '))
    b = 0
    k = []
    a = randint(1,1000)
    if a < 0:
        a = abs (a)
    else:
        a == a
    while a != o:
        i = o
        if i not in k:
            k.append (i)
        elif i in k:
            print('Вы повторяетесь')
            o = int(input ())
            continue
        b += 1
        if o > a:
            print(f'Загаданное число меньше, количество попыток: {b}')
        elif o < a:
            print(f'Загаданное число больше, количество попыток: {b}')
        o = int(input ())
    print(f'{name}, Вы угадали, это число {a} и Вы потратили {b+1} попыток')
    write_results (name, b)

    
def read_results():
    print(file_l.read())


def exiting():
    print('Okay, I"m exiting of the game')
    raise SystemExit

def process_input(choice):
    MENU[choice]()

MENU = {
    1: play,
    2: read_results,
    3: exiting
}
def main():
    while True:
        print_menu()
        choice = int(input ('Сделайте Ваш выбор пожалуйста: '))

        try:
            process_input(choice)
        except:
            print('Данного пункта в меню нет\nПовторите Ваш выбор: ')

main()



# final version

from random import randint


def print_menu():
    print('Menu: ')
    for k, value in MENU.items():
        print(f'{k} {value.__name__}')


def write_results(name, attempts):
    file_l = open('./Results.txt', 'a') 
    file_l.write(f'{name} had {attempts+1} trying \n')
    file_l.close()



def play():
    print('Good, lets go..')
    name = input('Представьтесь пожалуйста ')
    number = int(input('Предложите Ваше число: '))
    attempts = 0
    duplicate_values = []
    random_number = randint(1,1000)
    if random_number < 0:
        random_number = abs (random_number)
    else:
        random_number == random_number
    while random_number != number:
        i = number
        if i not in duplicate_values:
            duplicate_values.append (i)
        elif i in duplicate_values:
            print('Вы повторяетесь')
            number = int(input ())
            continue
        attempts += 1
        if number > random_number:
            print(f'Загаданное число меньше, количество попыток: {attempts}')
        elif number < random_number:
            print(f'Загаданное число больше, количество попыток: {attempts}')
        number = int(input ())
    print(f'{name}, Вы угадали, это число {random_number} и Вы потратили {attempts+1} попыток')
    write_results (name, attempts)

    
def read_results():
    file_l = open('./Results.txt', 'r+') 
    print(file_l.read())


def exiting():
    pass

def process_input(choice):
    MENU[choice]()

MENU = {
    1: play,
    2: read_results,
    3: exiting
}
def main():
    while True:
        print_menu()
        choice = int(input ('Сделайте Ваш выбор пожалуйста: '))
        if choice == 3:
            print('Okay, I"m exiting of the game')
            break
        else:
            try:
                process_input(choice)
            except:
                print('Данного пункта в меню нет\nПовторите Ваш выбор: ')

main()


