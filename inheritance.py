# Создайте новый проект или продолжите работу в текущем проекте
#
# Ваша задача:
#   Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
# которая возвращает количество лошидиных сил для автомобиля
#       Создайте наследника класса Car - класс Nissan и переопределите свойство price,
# а также переопределите функцию horse_powers
#       Дополнительно создайте класс Kia, который также будет наследником класса Car и переопределите также
# свойство price, а также переопределите функцию horse_powers
#
# Получившийся код прикрепите к заданию текстом


class Car:
    price = 1000000

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f'{self.__class__.__name__} {self.model} стоит {self.price} рублей'

    def horse_powers(self):
        print('и имеет 102 л/с')


class Nissan(Car):
    price = 500000

    def horse_powers(self):
        print('и имеет 125 л/с')


class Kia(Car):
    price = 650000

    def horse_powers(self):
        print('и имеет 132 л/с')


class Lada(Car):
    pass


teana = Nissan(model='TEANA')
rio = Kia(model='RIO')
vesta = Lada(model='VESTA')
print(teana)
teana.horse_powers()
print(rio)
rio.horse_powers()
print(vesta)
vesta.horse_powers()
