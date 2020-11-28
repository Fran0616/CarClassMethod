import car
def main():

    year_model = int(input("What year is the car: "))
    make = input("What is the car make: ")
    speed = 0

    mycar = Car(year_model, make, speed)

    #Accelerating 5 times
    mycar.accelerate()
    print("Current speed: ",mycar.get_speed())
    mycar.accelerate()
    print("Current speed: ",mycar.get_speed())
    mycar.accelerate()
    print("Current speed: ",mycar.get_speed())
    mycar.accelerate()
    print("Current speed: ",mycar.get_speed())
    mycar.accelerate()
    print("Current speed: ",mycar.get_speed()) 

    #Braking 5 times
    mycar.brake()
    print("The current speed  after brake: ",mycar.get_speed())
    mycar.brake()
    print("The current speed  after brake: ",mycar.get_speed())
    mycar.brake()
    print("The current speed  after brake: ",mycar.get_speed())
    mycar.brake() 
    print("The current speed  after brake: ",mycar.get_speed())
    mycar.brake()
    print("The current speed  after brake: ",mycar.get_speed())


main()
