import os
from fnmatch import fnmatch


def ls():
    list = os.listdir()
    return f'Содержание текущей директории: {list}'


class CustomContextManager:

    def __init__(self, file_name: str, text: str):
        self.file = open(file_name, mode='x')
        self.text = text

    def __enter__(self):
        self.file.write(self.text)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class Dir:
    def create_dir(self, direct):
        try:
            os.mkdir(direct)
            return f'Папка {direct} была успешно создана в директории {os.getcwd()}'
        except OSError:
            return f'Ошибка. Папка с именем: {direct} уже существует в данной директории {os.getcwd()}'

    def delete_dir(self, direct):
        try:
            os.rmdir(direct)
            return f'Папка {direct} была удалена в директории {os.getcwd()}'
        except FileNotFoundError:
            return f'Ошибка. Папки {direct} не существует в директории {os.getcwd()}'

    def rename_dir(self, old_dir, new_dir):
        try:
            os.rename(old_dir, new_dir)
            return f'папка {old_dir} была успешна переименована в {new_dir} в директории {os.getcwd()}'
        except FileNotFoundError:
            return f'Ошибка. Папки {old_dir} не существует в директории {os.getcwd()}'


slider = True
while slider:
    print('Добро пожаловать в CMD')
    base = os.getcwd()
    print(f'Директория файла Python: {base}')
    print('_________________________________________________________')
    print('Переход в директорию диска С: нажмите цифру [1]\n'
          'Выход из программы: нажмите цифру [0]\n')
    choice1 = input('команда: ')
    if choice1 == '0':
        print('Выход из программы')
        break
    elif choice1 == '1':
        slider = False
        os.chdir('/Users')           #Эта строка перекидывает в директорию USERS
        print(f'Директория диска С: {os.getcwd()}')
        print(ls())

        slider_inside = True
        while slider_inside:
            print('_________________________________________________________')
            print(f'Список команд: \n')
            print(f'Показать содержимое директории: напишите ls')  # Done
            print(f'Переход внутрь папки: напишите cd'"'название папки'")  # done
            print(f'Переход обратно: напишите back')  # done
            print(f'Работа с Папкой: [d]\nРабота с Файлом: [f]')  # done
            print(f'Просмотр файлов : [r]\n')  # done
            print(f'Выход из программы: [e]\n')  # done
            print('_________________________________________________________')

            a = input('Введите команду: ')
            if a == 'e':
                print(f'Выход из программы')
                break
            elif a == 'ls':
                print(f'Текущая директория: {os.getcwd()}')
                print(ls())

            elif a == 'cd':
                b = input('Введите название директории: ')
                try:
                    os.chdir(b)
                except FileNotFoundError:
                    print(f'Ошибка. Директории {b} не существует. Попробуйте снова')
                print(f'Текущая директория: {os.getcwd()}')
                print(ls())
            elif a == 'back':
                os.chdir('..')
                print(f'Текущая директория: {os.getcwd()}')
                print(ls())
            elif a == 'd':
                b = input('Создать папку: [1], удалить: [2], переименовать [3]: ')
                if b == '1':
                    b = Dir()
                    print(b.create_dir(direct=input('Введите название папки: ')))
                elif b == '2':
                    b = Dir()
                    print(b.delete_dir(direct=input('Введите название папки: ')))
                elif b == '3':
                    b = Dir()
                    print(b.rename_dir(old_dir=input('Введите текущее название: '),
                                       new_dir=input('Введите новое название: ')))
            elif a == 'f':
                b = input('Создать файл: [1], удалить: [2], переименовать [3]: ')
                if b == '1':
                    file_name = input('Введите название файла и формат (через точку) : ')
                    text = input('Введите текст файла: ')
                    try:
                        with CustomContextManager(file_name, text) as context_manager:
                            print(f'Файл {file_name} был создан в директории: {os.getcwd()}')
                    except FileExistsError:
                        print(f'Ошибка. Файл {file_name} уже существует в директории: {os.getcwd()}')
                elif b == '2':
                    try:
                        file = input('Введите название файла и формат (через точку): ')
                        os.remove(file)
                        print(f'Файл {file} был удален из директории {os.getcwd()}')
                    except FileNotFoundError:
                        print(f'Ошибка. Файл не найден в директории {os.getcwd()}')
                elif b == '3':
                    try:
                        file_name_from = input('Введите текущее название файла и формат (через точку): ')
                        file_name_to = input('Введите новое название файла и формат (через точку): ')
                        os.rename(file_name_from, file_name_to)
                        print(f'Файл {file_name_from} был переименован в {file_name_to} в директории {os.getcwd()}')
                    except FileNotFoundError:
                        print(f'Ошибка.  Файл не найден в директории {os.getcwd()}')
            elif a == 'r':
                try:
                    file_to_read = input('Введите название файла и формат (если необходимо!): ')
                    with open(file_to_read, mode='r') as file:
                        print(f'Содержимое файла {file_to_read}:\n{file.read()}')
                        file.close()
                except FileNotFoundError:
                    print(f'Ошибка. Файл не существует в директории: {os.getcwd()}')

    else:
        print('Ошибка. Попробуйте еще раз\n')
        continue
