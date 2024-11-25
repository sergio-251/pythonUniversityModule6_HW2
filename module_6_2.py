# Доступ к свойствам родителя. Переопределение свойств

class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'yellow', 'white', 'black']

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        if not color.lower() in self.__COLOR_VARIANTS:
            self.__COLOR_VARIANTS.append(color.lower())

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f'Владелец: {self.owner}', sep='\n')

    def set_color(self, color):
        if not color.lower() in self.__COLOR_VARIANTS:
            print(f'Нельзя сменить цвет на {color}')
        else:
            self.__color = color

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()

print(vehicle1._Sedan__PASSENGERS_LIMIT)



