import os
import shutil


#Создание новой папки
def create_folder():
    name = input('Название папки: ')
    if not os.path.isdir(name):
        os.makedirs(name)
    else:
        print('Папка с таким названием уже существует')
        main_menu()

#Создание нового файла
def create_file():
    name = input('Название файла (с расширением): ')
    file = open(name, 'w')

#Копирование файла/папки
def copy():
    name = input('Название файла/папки: ')
    folder_name = input('Введите папку, куда необходимо скопировать файл/папку: ')
    if os.path.isfile(name):
        shutil.copy2(name, folder_name)
    elif os.path.isdir(name):
        new_name = input('Новое имя: ')
        shutil.copytree(name, new_name)

#Перемещение файла/папки в другую папку
def move():
    name = input('Название файла/папки: ')
    folder_name = input('Введите папку, куда необходимо скопировать файл/папку: ')
    if os.path.isfile(name):
        shutil.move(name, folder_name)
    elif os.path.isdir(name):
        new_name = input('Новое имя: ')
        shutil.move(name, new_name)

#Удаление файла/папки
def delete():
    name = input('Название файла/папки: ')
    if os.path.isfile(name):
        os.remove(name)
    elif os.path.isdir(name):
        os.rmdir(name)

#Главное меню
def main_menu():
    while True:
        try:
            print('1 - Создать папку',
                  '2 - Создать файл',
                  '3 - Скопировать файл/папку',
                  '4 - Переместить файл/папку в другую папку',
                  '5 - Удалить файл/папку', sep='\n')
            choice = input('Выберете действие: ')
            break
        except:
            pass

    match choice:
        case '1':
            print('Создание папки')
            create_folder()
        case '2':
            print('Создание файла')
            create_file()
        case '3':
            print('Копирование файла/папки')
            copy()
        case '4':
            print('Перемещение файла/папки')
            move()
        case '5':
            print('Удаление файла/папки')
            delete()

print('Добро пожаловать в программу для работы с файлами и папками!')
main_menu()