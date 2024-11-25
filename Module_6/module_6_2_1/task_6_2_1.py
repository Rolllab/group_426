import os
import subprocess
from typing import TypeAlias

List: TypeAlias=list    # Можно, конечно и без этого, но проф-программисты сейчас опять смотрят в сторону typing

project_main_dir = os.path.abspath(os.path.join(os.getcwd(), ''))

folders = [i for i in os.listdir(project_main_dir) if os.path.isdir(os.path.join(project_main_dir, i))]

text_files = (
    os.path.abspath(os.path.join(project_main_dir, folders[0], 'text_1.txt')),
    os.path.abspath(os.path.join(project_main_dir, folders[0], 'text_2.txt')),
    os.path.abspath(os.path.join(project_main_dir, folders[1], 'text_3.txt')),
    os.path.abspath(os.path.join(project_main_dir, folders[1], 'text_4.txt'))
)

for file in text_files:
    if os.path.isfile(file):
        print(file)

# задание 2
print()
print('Задание 2:')
walk = [i for i in os.walk(project_main_dir)][0]
for i in range(3):
    print(', '.join(walk[i]) if type(walk[i]) is List else os.path.basename(walk[0]))

# Задание 3 выполнено в первом задании
# Задание 4
folder = 'folder_3'
# Самая бесполезная строка в моей кодовой жизни (если каталог есть - удаляем его, если нет - создаем)
subprocess.run(['mkdir', folder] if subprocess.run(['test', '-d', folder]).returncode != 0 else ['rmdir', folder])
