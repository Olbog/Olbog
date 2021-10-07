'''

2 Напиши программу которая принимает в аргументы программы имя(путь) к файлу
                        - Если такой файл существует напечатать следующую информацию о нем:
                        - Имя файла
                        - (полный путь к файлу)
                        - Дата создания файла
                        - размер файла
                        - первые 5 строк содержимого и троеточие в конце(если в файле более 5 строк)

                        Если это дериктория вывести соответствующее сообщение и показать следующую информацию:
                        - Название деректории
                        - (полный путь к директории)
                        - Количество файло в дериктории/количество папок в дериктории
                        - список файло в директории

Для написания такой утилиты используют такие модули как os(для работы с файлами) и sys(для работы с аргументами программы - 
почитай про sys.args / argparse)

'''

import os
import datetime

path_in_file = input('Введите путь к файлу: \n')

info_file_menu = {
    'Имя данного файла:' : os.path.basename(path_in_file),
    'Путь к данному файлу:'  : os.path.abspath(path_in_file),
    'Размер данного файла:'  : os.stat(path_in_file).st_size,
    'Файл был создан:'  : datetime.datetime.fromtimestamp(os.path.getmtime(path_in_file))
}

def file_info(a):
    for k, value in info_file_menu.items():
        print(f'{k} {value}')

    with open(path_in_file, 'a+') as file:
        file.seek(0)
        line_count = 0
        for line in file:
            if line_count < 5:
                print(line[:-2])
            elif line_count >= 6:
                file.seek(2)
                print('...')
                break
            line_count +=1

def dir_info(a):

    info_dir_menu = {
        'Название данного каталога : ' : os.path.basename(path_in_file),
        'Полный путь к каталогу: ' : os.path.realpath(path_in_file),
        'Список файлов и папок в каталоге: ' : os.listdir(os.path.abspath(path_in_file)),
        'Количество вложенных файлов равно: ' : len(os.listdir(path_in_file))
    }

    print('Это каталог! ')
    for k, value in info_dir_menu.items():
        print(f'{k} {value}')
    


if os.path.isfile(path_in_file):
    file_info(path_in_file)
elif os.path.isdir(path_in_file):
    dir_info(path_in_file)




