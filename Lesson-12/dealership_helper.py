# Python Object Oriented Programming

# Creating a class
# class ClassName:


class Car:
    """This is a Car Class. A car has a make, model, year, and price. the price is private.
    The odometer reading is public.

    Returns:
        [type] -- [description]
        Car: A Car Object
    """

    # create a car constructor (build the blueprint)
    # notice the double underscore __init__
    # this is a dunder method
    # Class Constructor - the method that is called when you create a new object
    # Class Attributes - variables that are shared by all instances of a class. All attributes a car has.
    def __init__(self, make, model, year, price):
        self.make = make  # this is an instance attribute
        self.model = model  # this is an instance attribute
        self.year = year  # this is an instance attribute
        self.__price = price  # this is a private instance attribute
        self.odometer_reading = 0  # this is a public instance attribute

    # Self is a reference to the current instance of the class. It is used to access variables that belong to the class.

    # Notice how when we tried to print the car1 object, we got a memory address.
    # This is because we have not defined a string representation for the Car class. T
    # The __str__ method is used to define a string representation for the class.
    # This is called a to_string method in java
    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.odometer_reading}"

    # create a method to get the price of the car
    # this is commonly referred to as a getter method in java

    @property  # this is a decorator. Decorators are used to modify the behavior of functions or classes.
    # Getter
    def price(self) -> int:
        """returns the price of the car object

        Returns:
            int: the price of the car
        """
        return self.__price

    # create a method to set the price of the car
    # this is commonly referred to as a setter method in java

    @price.setter  # decorator that allows you to set the price of the car
    # Setter
    def price(self, new_price) -> int:
        """sets the price of the car object

        Args:
            new_price (int): the new price of the car
        """
        self.__price = new_price

    # Class Methods - these are the methods that all cars will have

    # create a method that updates the odometer reading
    def update_odometer(self, milage: int):
        """update the odometer reading to the new milage

        Args:
            milage (int): the new milage
        """
        if milage > self.odometer_reading and milage > 0:
            self.odometer_reading = milage  # update the odometer reading
        else:
            print("You can't roll back an odometer!")
