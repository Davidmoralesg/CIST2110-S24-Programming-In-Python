# import dealership healper to build car objects
from dealership_helper import Car, ElectricCar


# from the Car class, we are inheriting all the attributes and methods

# from the Car class, create a car Object

car1 = Car("Toyota", "Camry", 2020, 25000)
car2 = Car("Honda", "Accord", 2019, 30000)

print(car1)  # <dealership_helper.Car object at 0x102b5eb10>
print(car1.make)
print(car1.odometer_reading)
# print(car1.__price)  # this will throw an error because __price is a private attribute


# print(car1.__doc__)  # this will print the docstring of the Car class

print(car1.price)

car1.price = 30000

print(car1.price)

car1.update_odometer(1000)
print(car1.odometer_reading)


print(car2.price)
print(car2.odometer_reading)
car2.update_odometer(20000)
print(car2.odometer_reading)


car1.increment_odometer(500)


print(car1.odometer_reading)


car_electric = ElectricCar("Tesla", "Model S", 2021, 80000, 1000)


print(car_electric)


print(car_electric.describe_battery())
