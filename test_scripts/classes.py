#classes in Python

class Car:
    wheels = 4
    def __init__(self, color): #"__init__()" method initializes the instance variables
        self.running = False
        self.color = color
    def start_engine(self): #"self" is the instance which calls the method 
        self.running = True #"running" is an instance variable
        print('engine started')

my_car = Car("blue") #initialize the instance my_car, belonging to the Car class
my_car.start_engine() #invokes the function

#Cookie class
#can take a list of ingredients as an input
#has a method which diplay the first of the ingredients
class Cookie:
    def __init__(self, ingredients):
        self.recipe = ingredients
    def getFlavour(self):
        return self.recipe[0]

listOfIngredients = ["milk", "honey", "chocolate"]
myCookie = Cookie(listOfIngredients)
mainFlavour = myCookie.getFlavour()
print("this cookie tastes like " + mainFlavour)

#class (Food) and subclass (Sandwich)
class Food:
    def __init__(self, ingredients):
        self.recipe = ingredients
    def getFlavour(self):
        return self.recipe[0]

class Sandwich(Food):
    def __init__(self, ingredients):
        Food.__init__(self, ingredients)    #within the function definition, I have to specify
                                            #the "self" parameter when invoking a function
    def getFlavour(self): #for the Sandwich subclass, this function overrides the same function of the Food parent class
        return ", ".join(self.recipe[1:]) #joins the list elements separating them with a ", "

listOfStuff = ['bread', 'cheese', 'lettuce', 'ham']
mySandwich = Sandwich(listOfStuff)
print(mySandwich.getFlavour())
