# Домашнее задание по уроку "Перегрузка операторов"

#   Создайте новый проект в PyCharm
#   Запустите созданный проект
# Ваша задача:
#   Создайте новый класс Buiding
#   Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут этажности self.numberOfFloors и строковый атрибут self.buildingType
#   Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашему заданию


class Building:


    def __init__(self, buildingType, numberOfFloors):
        self.buildingType = buildingType
        self.numberOfFloors = numberOfFloors

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


my_building = Building(buildingType='1', numberOfFloors=15)
notmy_building = Building(buildingType='1', numberOfFloors=15)

if Building.__eq__(self=my_building, other=notmy_building):
    print('Мы похожи')
else:
    print('нет')