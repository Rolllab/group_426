class Employer:
    def __init__(self, name=None, lastname=None, age=None, position=None):
        self.__name = name
        self.__lastname = lastname
        self.__age = age
        self.__position = position

    @property
    def get_name(self):
        return self.__name

    @property
    def get_lastname(self):
        return self.__lastname

    @property
    def get_age(self):
        return self.__age

    @property
    def get_position(self):
        return self.__position

    @staticmethod
    def print_():
        return 'This is Employer class'


class President(Employer):
    def __init__(self, name, lastname, age, position):
        super().__init__(name=name, lastname=lastname, age=age, position=position)

    def print_(self):
        return f'Name = {self.get_name}\nlastname = {self.get_lastname}\nage={self.get_age}\nPosition = {self.get_position}'


class Manager(Employer):
    def __init__(self, name, lastname, age, position):
        super().__init__(name=name, lastname=lastname, age=age, position=position)

    def print_(self):
        return f'Name = {self.get_name}\nlastname = {self.get_lastname}\nage={self.get_age}\nPosition = {self.get_position}'


class Worker(Employer):
    def __init__(self, name, lastname, age, position):
        super().__init__(name=name, lastname=lastname, age=age, position=position)

    def print_(self):
        return f'Name = {self.get_name}\nlastname = {self.get_lastname}\nage={self.get_age}\nPosition = {self.get_position}'


if __name__ == '__main__':
    # Данные
    names = ['Oleg', 'Barbara', 'John']
    lastnames = ['Tinkoff', 'Brown', 'Douglas']
    ages = [54, 35, 28]
    positions = ['president', 'manager', 'worker']
    classes = [President, Manager, Worker]

    # Для вывода записи - This is Employer class
    employer = Employer()
    print(employer.print_())

    # Цикл для пробежки по данным
    for i in range(len(names)):
        job = classes[i](name=names[i], lastname=lastnames[i], age=ages[i], position=positions[i])
        print(job.print_())
        print()
