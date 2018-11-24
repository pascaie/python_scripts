#classes in Python

class Car:
    wheels = 4
    def start_engine(self):
        self.running = True
        print('engine started')

my_car = Car() #initialize the instance my_car, belonging to the Car class
my_car.start_engine() #invokes the function
