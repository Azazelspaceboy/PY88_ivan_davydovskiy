class Auto:
    def __init__(self, brand: str, age: int, colour: str):
        self.brand = brand
        self.age = age
        self.colour = colour

    def start(self):
        print("move")
    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


class Car(Auto):
    def __init__(self, max_speed: int, brand: str, age: int, colour: str):
        super().__init__(brand, age, colour)
        self.max_speed = max_speed


    def move(self):
        self.start()
        print(f"max speed is: {self.max_speed}")


class Truck(Auto):
    def __init__(self, max_load: int, brand: str, age: int, colour: str):
        super().__init__(brand, age, colour)
        self.max_load = max_load


    def move(self):
        print("attention")
        self.start()


car = Auto("BMW", 19, "blue")
car.birthday()
print(car.age)
car.start()
car.stop()
some = Car(99, "Bmw", 20, "red")
some.move()
truck = Truck(100, "asd", 20, "green")
truck.move()
