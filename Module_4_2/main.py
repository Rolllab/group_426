from Module_4_2.My_module import my_module_1, my_module_2
from Module_4_2.My_module_2 import my_module_2_file_1, my_module_2_file_2
from Module_4_2.My_module_2.folder_1 import folder_1_file_2, folder_1_file_1
from Module_4_2.My_module_2.folder_1.folder_2 import folder_2_file_2, folder_2_file_1
from Module_4_2.My_module_2.folder_1.folder_2.folder_3 import folder_3_file_2, folder_3_file_1

"""Не знаю, правильно ли я понял задание"""

print(folder_3_file_1.get_address())
print(folder_3_file_2.get_address())
print(folder_2_file_1.get_address())
print(folder_2_file_2.get_address())
print(folder_1_file_1.get_address())
print(folder_1_file_2.get_address())
print(my_module_2_file_1.get_address())
print(my_module_2_file_2.get_address())
print(my_module_1.get_address())
print(my_module_2.get_address())