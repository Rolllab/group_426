class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self, stack_size=5, top=None):
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        """Принимает значение в стек, проверяет возможность добавления в стек
            и если такая возможность есть - добавляет его присваивая обновленное
            значение node. Если не принимает значение, то возвращает запись -
            стек переполнен."""
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            print("Стэк переполнен")
            return "Стэк переполнен"

    def pop(self):
        """Удаляет из стека последнее значение при этом делая его возврат.
            И переназначает node-у"""
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    def is_empty(self):
        """Возвращает True - если стек пустой.
            Возвращает False - если в стеке что-то есть"""
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        """Возвращает True - если стек заполнен до отказа.
           Возвращает False - если это не так"""
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):
        """Метод очищает стек"""
        while self.top:
            self.pop()

    def get_data(self, index):
        """Возвращает донные, которые идут под номером индекса (data)
            Если индекс не входит в диапазон, то возвращает - Out of range"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):
        """Возвращает количество элементов в стеке"""
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        """Возвращает количество элементов, которые имеют тип integer"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter


stack = Stack()
stack.push(1)
stack.push("sta")
stack.push(2)
stack.push(2.5)
stack.push("sta")
print(stack.counter_int())