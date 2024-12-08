class Employer:
    def __init__(self, name=None, lastname=None, age=None, position=None):
        self.__name = name
        self.__lastname = lastname
        self.__age = age
        self.__position = position

    def __str__(self):
        return dict(Name=self.__name, Lastname=self.__lastname, Age=self.__age, Position=self.__position)

    @staticmethod
    def print_():
        return 'This is Employer class'


class President(Employer):
    def __str__(self):
        return f"President: {super().__str__()}"


class Manager(Employer):
    def __str__(self):
        return f"Manager: {super().__str__()}"


class Worker(Employer):
    def __str__(self):
        return f"Worker: {super().__str__()}"


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
    print()

    # Цикл для пробежки по данным
    for i in range(len(names)):
        job = classes[i](name=names[i], lastname=lastnames[i], age=ages[i], position=positions[i])
        print(job)  # Используется __str__()
