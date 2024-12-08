class Wheels:
    def __init__(self, diameter, width):
        self.__diameter = diameter
        self.__width = width

    @property
    def get_diameter(self):
        return self.__diameter

    @property
    def get_width(self):
        return self.__width

    @get_diameter.setter
    def get_diameter(self, item):
        self.__diameter = item

class Engine:
    def __init__(self, type_, power):
        self.__type = type_
        self.__power = power

    @property
    def get_type(self):
        return self.__type

    @property
    def get_power(self):
        return self.__power

    @get_type.setter
    def get_type(self, item):
        self.__type = item

class Doors:
    def __init__(self, side_door, color):
        self.__side_door = side_door
        self.__color = color

    @property
    def get_side_door(self):
        return self.__side_door

    @property
    def get_color(self):
        return self.__color

    @get_side_door.setter
    def get_side_door(self, item):
        self.__side_door = item

class Car:
    def __init__(self, wheels:object=Wheels, engine:object=Engine, doors:object=Doors):
        self.wheels = wheels
        self.engine = engine
        self.doors = doors

    def get_data(self):
        return {
            'diameter_wheels': self.wheels.get_diameter,
            'width_wheels': self.wheels.get_width,
            'type_engine': self.engine.get_type,
            'power_engine': self.engine.get_power,
            'side_doors': self.doors.get_side_door,
            'color_doors': self.doors.get_color
        }


if __name__ == '__main__':
    wheels_ = Wheels(diameter=15, width=210)
    engine_ = Engine(type_='gasoline', power=210)
    doors_ = Doors(side_door='left', color='blue')
    car = Car(wheels_, engine_, doors_)

    print(car.get_data())
