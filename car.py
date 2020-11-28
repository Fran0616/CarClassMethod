#Francisco Francillon
class Car:
    def __init__(self, year_model,make,speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def set_year_model(self, year):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = 0

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    #The accelerate method should add 5 to the speed data attribute each time it is called. brake
    def accelerate(self):
        self.__speed +=5
        #The brake method should subtract 5 from the speed data attribute each time it is called. get_speed
    def brake(self):
        self.__speed -=5
        #The get_speed method should return the current speed.
    def get_speed(self):
        return self.__speed
