#modules

#import datetime module and use its date() function
import datetime
birthday = datetime.date(1992, 7, 17)
print("I was born on " + str(birthday))

#import specific functions
from datetime import date, time as t
sisterBirthday = date(1997,6,11) #can invoke the date() function without specifying the parent module
print("My sister was born on " + str(sisterBirthday))
date.today()
print("Today is " + str(date.today()))

setTime = t(19, 35, 50)
print(setTime)
print(setTime.hour)

import sys #module of system-specific parameters and functions
print(sys.path) #displays the paths which are followed by the Python engine when searching for packages/modules

import actionPackage.action
actionPackage.action.printSomething()

import printModule
printModule.printWord("ciao")

