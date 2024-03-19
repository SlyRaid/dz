# Создайте новый проект или продолжите работу в текущем проекте
#
# Ваша задача:
#       Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
#       Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
# которая возвращает количество лошидиных сил для автомобиля
#       Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
# а также переопределите функцию horse_powers
#       Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price
# Получившийся код прикрепите к заданию текстом

class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f'{self.__class__.__name__} {self.model} стоит {self.price} рублей'

    def horse_powers(self):
        print('102 л/с')


class Nissan(Car, Vehicle):
    price = 500000
    vehicle_type = 'passenger car'

    def horse_powers(self):
        print('125 л/с')



teana = Nissan(model='TEANA')
print(teana.vehicle_type, teana.price)
teana.horse_powers()