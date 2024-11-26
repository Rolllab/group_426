class Vehicle:
    def __init__(self, name:str, mileage:int):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, amt_wheels:int):
        if amt_wheels == 2:
            return f'Это мотоцикл марки {self.name}'
        if amt_wheels == 3:
            return f'Это три-цикл марки {self.name}'
        if amt_wheels == 4:
            return f'Это автомобиль марки {self.name}'
        return False

    def get_vehicle_advice(self):
        if self.mileage <= 50000:
            return f'Неплохо {self.name} можно брать.'
        elif 50001 < self.mileage <= 100000:
            return f'{self.name}) надо внимательно проверить.'
        elif 100001 < self.mileage <= 150000:
            return f'{self.name} надо провести полную диагностику.'
        else:
            return f'{self.name} лучше не покупать.'


if __name__ == '__main__':
    audi = Vehicle(name='audi', mileage=500000)
    bmw_tricycle = Vehicle(name='bmw_tricycle', mileage=150000)
    vw = Vehicle(name='vw', mileage=5)
    aston_martin = Vehicle(name='audi', mileage=0)
    bike = Vehicle(name='kawasaki', mileage=25000)

    list_vehicle = [audi, bmw_tricycle, vw, aston_martin, bike]
    list_wheels = [4, 3, 4, 4, 2]

    for item in range(len(list_vehicle)):
        print(list_vehicle[item].get_vehicle_type(list_wheels[item]))
        print(list_vehicle[item].get_vehicle_advice())
        print('-' * 50)
