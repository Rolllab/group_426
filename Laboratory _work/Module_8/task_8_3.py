class HomeAnimals:
    def __init__(self, name):
        self.__name = name

    @property
    def get_name(self):
        return self.__name

# Из-за множественного дублирования кода создал этот класс
class Property:
    def __init__(self, sound, type_):
        self.__sound = sound
        self.__type = type_

    @property
    def get_sound(self):
        return self.__sound

    @property
    def get_type(self):
        return self.__type

class Dog(HomeAnimals):
    def __init__(self, name):
        super().__init__(name=name)
        self.__sound = 'гав'
        self.__type = 'собака'

    def get_property(self):
        return Property(self.__sound, self.__type)

class Cat(HomeAnimals):
    def __init__(self, name):
        super().__init__(name=name)
        self.__sound = 'мяу'
        self.__type = 'кошка'

    def get_property(self):
        return Property(self.__sound, self.__type)

class Parrot(HomeAnimals):
    def __init__(self, name):
        super().__init__(name=name)
        self.__sound = 'чирик'
        self.__type = 'попугай'

    def get_property(self):
        return Property(self.__sound, self.__type)


class Hamster(HomeAnimals):
    def __init__(self, name):
        super().__init__(name=name)
        self.__sound = 'фырк'
        self.__type = 'хомяк'

    def get_property(self):
        return Property(self.__sound, self.__type)


if __name__ == '__main__':
    names = ['Дружок', 'Барсик', 'Кеша', 'Хомяк']
    classes = [Dog, Cat, Parrot, Hamster]
    for index in range(len(names)):
        animal = classes[index](names[index])
        property_ = animal.get_property()

        print(f'Имя: {animal.get_name}')
        print(f'Тип: {property_.get_type}')
        print(f'Звук: {property_.get_sound}')
        print()
