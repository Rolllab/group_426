import os
import sys

def write_to_file(string):
    text_foo = [f'{i.capitalize()}' for i in string.split(', ')]
    with open(path_to_file, 'a', encoding='utf-8') as file:
        for i in text_foo:
            if i == text_foo[-1]:
                file.write(i)
            else:
                file.write(f'{i},\n')
    return True

def read_file():
    with open(path_to_file, encoding='utf-8') as file:
        return sys.stdout.write(file.read())



if __name__ == '__main__':
    path_to_file = os.path.abspath(os.path.join(os.getcwd(), '../module_6_2_1/folder_1/text_1.txt'))
    text = 'Если б мишки были пчелами, то они бы нипочем, никогда и не подумали, так высоко строить дом.'
    write_to_file(text)
    read_file()
