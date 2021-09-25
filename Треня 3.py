# print ('The Menu of this game:\n 1. Play\n 2. View the results\n 3. Exit')
# choice = int(input ('Сделайте Ваш выбор пожалуйста'))
# if choice == 1:
#     print ('Good, lets go..')
# elif choice == 2:
#     open ('./Results.txt', 'r')
# else:
#     print('Okay, I"m exiting of the game')
#     raise SystemExit



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

