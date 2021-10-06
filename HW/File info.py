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

path_in_file = input('Введите путь к файлу или каталогу: \n')


def file_info(path_in_file):
    file_path = os.path.splitext(path_in_file)[0]
    file_size = os.stat(path_in_file).st_size
    file_time = os.path.getmtime(path_in_file)
    file_full_time = datetime.datetime.fromtimestamp(file_time)
    file_full_name = os.path.basename(path_in_file)
    file_name = os.path.splitext(file_full_name)[0]

    print('\nИмя данного файла: ', file_name)
    print('Путь к данному файлу: ', file_path)
    print('Размер данного файла: ', file_size)
    print('Файл был создан: ', file_full_time, '\n')
    
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
            

# def directory_info(path_in_file):
#     print('Это директорий! ')
#     way = os.path.dirname(__file__)
#     print(way)



        
for i in path_in_file:
    try:
        file_info(path_in_file)
    # except:
    #     try:
    #         print()
    except:
        print('Данного файла не существует..')
    break



