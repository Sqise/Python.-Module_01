# Создайте инициализатор для класса House, который будет задавать атрибут
# этажности self.numberOfFloors = 0
# Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут
# numberOfFloors на параметр floors и выводить в консоль numberOfFloors

class House:

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


house1 = House()
house1.setNewNumberOfFloors(10)
