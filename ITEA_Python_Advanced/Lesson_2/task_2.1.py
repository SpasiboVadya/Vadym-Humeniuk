class Vehicle:

    def __init__(self, brand, model, clas, color, engine, year, price):
        self.brand = brand
        self.model = model
        self.clas = clas
        self.color = color
        self.engine = engine
        self.year = year
        self.price = price


class Car(Vehicle):

    def __init__(self, brand, model, clas, color, engine, year, price, speed_of_acceleration, max_speed):
        super().__init__(brand, model, clas, color, engine, year, price)
        self.speed_of_acceleration = speed_of_acceleration
        self.max_speed = max_speed


class Truck(Vehicle):

    def __init__(self, brand, model, clas, color, engine, year, price, car_weight, max_weight):
        super().__init__(brand, model, clas, color, engine, year, price)
        self.car_weight = car_weight
        self.max_weight = max_weight


Car1 = Car('Mercedes-Benz', 'E250', 'E - Class', 'White', 'Diesel 2.5', 2014, '27 900 $', '160/4', 220)
Car2 = Car('BMW', 'M235i', 'A - Class', 'Blue', 'Gasoline 326/240', 2016, '37 000 $', '290/4', 320)
Truck1 = Truck('Mercedes-Benz', 'Sprinter 316', 'E - class', 'White', 'Diesel 2.1', 2016, '18 800 $ ', 4,  1000)
