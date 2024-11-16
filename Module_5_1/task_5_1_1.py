from functools import partial

"""Ох и замороченные задания пошли..."""

literary_genre = ('Роман', 'Новелла', 'Фэнтези', 'Научная Фантастика')
numbers_tuple = (3, 7, 9, 1, 6, 8, 2, 5, 4)

list_tuple = [literary_genre, numbers_tuple]
tasks = ['Длина кортежа', 'Максимальный элемент', 'Минимальный элемент', 'Сумма элементов', 'Сортировка по возрастанию', 'Сортировка по убыванию']
actions = [len, max, min, sum, sorted, partial(sorted, reverse=True)]

for i in list_tuple:
    print('Кортеж - ', i)
    for item in range(len(tasks)):
        try:
            if actions[item] is sorted or item == len(actions)-1:
                print(f'\t{item + 1}. {tasks[item]} = ', tuple(actions[item](i)))
            else:
                print(f'\t{item+1}. {tasks[item]} = ', actions[item](i))
        except TypeError:
            print(f'\t{item+1}. Просуммировать элемент не возможно!!!')

    print()
