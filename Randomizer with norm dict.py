from random import randint
file_l = open('./Results.txt', 'a') 

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
        try:
            process_input(choice)
        except:
            print('Данного пункта в меню нет\nПовторите Ваш выбор: ')

main()

