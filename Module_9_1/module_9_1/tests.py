import unittest

from Module_9_1.Stack import Stack

list_ = [1, 2, 3, 4, 5]

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(10)
        self.assertEqual(self.stack.get_data(0), 10)    # Тестируем data
        self.assertEqual(self.stack.top.data, 10)       # Тестируем вершину
        for number, i in enumerate(list_):
            if number  == 4:
                self.assertEqual(self.stack.push(i), 'Стэк переполнен') # Тестируем else
            self.stack.push(i)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 'Стэк пуст') # Тестируем else
        self.stack.push(10)    # Добавляем в стек значение
        self.stack.pop()        # Удаляем из стека значение
        self.assertEqual(self.stack.pop(), 'Стэк пуст')  # Тестируем функцию pop()

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True) # Тест на пустоту
        self.stack.push(10)     # Добавляем в стек значение
        self.assertEqual(self.stack.is_empty(), False)  # Тест на значение

    def test_is_full(self):
        self.assertEqual(self.stack.is_full(), False)   # Тест на пустоту
        for i in list_:
            self.stack.push(i)  # Добавляем в стек значение
        self.assertEqual(self.stack.is_full(), True)    # Тест на равенство

    def test_clear_stack(self):
        for i in list_:
            self.stack.push(i)  # Добавляем в стек значение
        self.stack.clear_stack()    # Очищаем стек
        self.assertEqual(self.stack.is_empty(), True)   # Проверяем как удалили

    def test_get_data(self):
        self.assertEqual(self.stack.get_data(1), 'Out of range')    # Если список пустой, то и результат будет соответствующий
        for i in list_:
            self.stack.push(i)
        self.assertEqual(self.stack.get_data(1), 4)     # Теперь цифра 4 имеет индекс 1, чудеса...))

    def test_size_stack(self):
        for i in range(3):
            self.stack.push(i)
        self.assertEqual(self.stack.size_stack(), 3)

    def test_counter_int(self):
        for i in ['123', 3, 5, 'asd', 3]:
            self.stack.push(i)
        self.assertEqual(self.stack.counter_int(), 3)   # Вернуло количество целых чисел
