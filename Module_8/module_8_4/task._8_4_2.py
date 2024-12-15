import os.path

def foo(text) -> bool:
    input_ = input(f'{text} -> ')
    if input_.lower().startswith('y') or input_.lower().startswith('д'):
        return True
    return False


class Cpu:
    def __init__(self, on=None):
        self.frequency:int = cpu_frequency
        self.core:int = core
        self.on = on

    def messages(self):
        return f'В CPU передано {self.on} Вт'

    def activate_turbo_mode(self, turbo=None):
        if turbo:
            self.frequency = cpu_turbo_frequency
            self.core = turbo_core
            return f'\nВнимание!!! Включен режим TURBO\nЧастота процессора = {self.frequency} GHz\nКоличество ядер = {self.core}'
        return f'\nТехнические характеристики остались без изменений:\nЧастота процессора = {self.frequency} GHz\nКоличество ядер = {self.core}'

    @staticmethod
    def handler_data(data:str):
        data = f'{data} + new function'
        return f'Обработанные данные - {data}'


class Ram:
    def __init__(self, on=None):
        super().__init__()
        self.memory = memory
        self.frequency:int = ram_frequency
        self.on = on

    def messages(self):
        return f'В RAM передано {self.on} Вт'

    def load_data(self):
        return f'\nЗагружены какие-то данные из процессора.\nНа частоте - {self.frequency} Гц.\nПамять ОЗУ (в размере - {self.memory} Гб) уменьшилась на 50 байт'

    def upload_data(self):
        return f'\nВыгружены очень важные данные в процессор.\nНа частоте - {self.frequency} Гц.\nПамять ОЗУ (в размере - {self.memory} Гб) увеличилась на 1075 байт'


class Ssd:
    def __init__(self, on=None):
        self.volume = volume_ssd
        self.on = on

    def messages(self):
        return f'В SSD передано {self.on} Вт'

    def save_data(self, file):
        size = os.path.getsize(os.path.abspath(os.path.join('module_8_4', file)))
        self.volume = self.volume + size
        return f'\nОбъем данных на диске увеличился на {size} байт и составляет {self.volume} байт.'

    def remove_data(self, file):
        size = os.path.getsize(os.path.abspath(os.path.join('module_8_4', file)))
        self.volume = self.volume - size
        return f'Объем данных на диске уменьшился на {size} байт и составляет {self.volume} байт.'


class VideoCards:
    def __init__(self, on=None):
        self.video_card:str = video_card_name
        self.memory_card:int = video_card_memory
        self.on = on

    def messages(self):
        return f'В видеокарту передано {self.on} Вт'

    def show_picture(self):
        return f'\nВидеокарта ({self.video_card}) с объемом памяти {self.memory_card} Гб вывела изображение на экран'


class Motherboard:
    def __init__(self, on=None):
        self.chipset:str = chipset
        self.power:int = power
        self.on = on

    def redistribution_energy(self):
        if self.chipset:
            print(f'\nМатеринская плата с чипсетом "{self.chipset}" получила энергию от блока питания в количестве {self.power} Вт')
            for i in list_classes:
                size_power = int(self.power/len(list_classes))
                print(i(on=size_power).messages())
            return
        return


class PowerUnit:
    def __init__(self, on=None):
        self.motherboard = Motherboard(on=True)
        self.power:int = power
        self.on = on

    def get_power(self):
        if self.on:
            print(f'\nВы включили компьютер!!!\nПотребление компьютера = {self.power} Вт')
            self.motherboard.redistribution_energy()
        return f'Питание компьютера выключено'


class MyPc:
    def __init__(self):
        self.cpu = Cpu()
        self.ram = Ram()
        self.ssd = Ssd()
        self.video_card = VideoCards()

    def start_modules(self):
        # Включаем блок питания и подаем напряжение не все блоки
        power_unit_on = PowerUnit(on=True)
        power_unit_on.get_power()

        # Нужен ли Turbo режим ?
        print(self.cpu.activate_turbo_mode(turbo=True) if foo('\nВы хотите активировать turbo-режим? y/n -> ')
              else self.cpu.activate_turbo_mode(turbo=False))

        # оперативная память.
        print(self.ram.load_data())                     # Загрузка данных
        print(self.ram.upload_data())                   # Выгрузка данных

        # SSD накопитель
        print(self.ssd.save_data('file.txt'))           # Сохранение данных
        print(self.ssd.remove_data('file.txt'))         # Удаление данных

        # Видео карта
        print(self.video_card.show_picture())                  # Показ изображения



if __name__ == '__main__':
    power = 650
    memory = 96
    volume_ssd = 100
    cpu_frequency, cpu_turbo_frequency = 2300,  3200
    ram_frequency = 1333
    core, turbo_core = 8, 20
    video_card_name = 'NVIDIA 3060'
    video_card_memory = 16
    chipset = 'Intel Z590'
    list_classes = [Cpu, VideoCards, Ram, Ssd]

    if foo('Включить компьютер? y/n -> '):
        my_pc = MyPc()
        my_pc.start_modules()
    else:
        power_unit_off = PowerUnit()
        print(power_unit_off.get_power())
