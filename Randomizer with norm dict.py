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

