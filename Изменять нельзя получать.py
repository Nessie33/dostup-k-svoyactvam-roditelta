class Vehicle:

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return 'Модель: ' + self.__model

    def get_horsepower(self):
        return 'Мощность двигателя: ' + f'{self.__engine_power}'

    def get_color(self):
        return 'Цвет: ' + f'{self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец: ' + self.owner)

    def set_color(self, new_color):
        new_color = new_color.lower()
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print('Нельзя сменить цвет на ' + new_color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
