# '''

# Basic of OOP (Classes, objects, attributes, and methods)

# Classes: Blueprint or template
# Object: copy of blueprint or template / child of blueprint
# attributes: variable of the class or objects
# methods: a function under a class

# '''

# class Vehicle:
#     horn = "Beep Beep" #attribute
#     def start(self): #in class all methods must have self as parameter (must)
#         print(self,"Self")
#         print("The vihicle is now on.")

# toyta = Vehicle() #object location is same as Vehicle
# audi = Vehicle() #not same location
# # same parent but different child

# print(toyta.horn)
# print(toyta,"Object") #same output as print(self)
# toyta.start() #already using toyota location is passed automatically.
# #saved in different memory.

# #toyota and Vihicle is not same.

# '''
# Principle of OOP
# 1. Inheritance (main)
# 2. Polymorphism (poly - multi morphism - shape)
# 3. Abstruction
# 4. Encapsulation
# '''

# #Inheritance

# class Car:
#     horn = "Beep Beep"
#     def __init__(self): #constractor #makes an object #If written means we want to add something.
#         print("An object is created") #auto runs when.
#         self.wheels = 4 #This will also be created for the object auto.
#         self.windows = 4 #Only for child.
#     def start(self):
#         print("The vihicle is now on.")

# toyta = Car() #this is created.
# audi = Car()
# #__init__ object is saved in toyota. __init__ is ran auto even if not written.
# # init will ran as many times as object is created.

# # print(Car.horn)
# # print(toyta.horn)
# # print(audi.horn)

# # Car.horn = "Vrom Vrom"
# # #_______________________________

# # print(Vehicle.horn)
# # print(toyta.horn)
# # print(audi.horn)

# # toyta.horn = 'beep' #

# # print(Vehicle.horn)
# # print(toyta.horn)
# # print(audi.horn)


# #______________________

# toyta = Car()
# audi = Car()

# print(toyta.wheels)

# audi.wheels = 3
# print(audi.wheels)

# # print(Vehicle.wheels) vehical as no attributes


'''
Class inheriting another class
'''

#inheritance class level


# class Vehicle:
#     horn = "Beep Beep"
#     def __init__(self):
#         self.wheels = 4 
#         self.windows = 4 
#     def start(self):
#         print("The vihicle is now on.")

# class Toyota(Vehicle):
#     #we can link this two class using inheritance by uing (class)
#     def stop(self):
#         print("Stop")

# my_toyota = Toyota()
# my_toyota.start()


'''Polymorphism'''

# class Vehicle:
#     horn = "Beep Beep"
#     def __init__(self):
#         print("An object is created")
#         self.wheels = 4 
#         self.windows = 4 
#     def start(self):
#         print("The vihicle is now on.")

# class Toyota(Vehicle):
#     #we can link this two class using inheritance by uing (class)
#     def start(self):
#         super().start()#will run both starts.
#         print("The toyota is on.")
#     def stop(self):
#         print("Stop")

# my_toyota = Toyota()
# my_toyota.start() #The toyota one will run.


'''There are other functions like __init__ those runs auto like it.

They are referred to as magic function

'''

# class Vehicle:
#     horn = "Beep Beep"
#     def __init__(self):
#         print("An object is created")
#         self.wheels = 4 
#         self.windows = 4 

#     def __str__(self): #runs whe I want to print the object.
#         return str(self.wheels) + ' Wheeler'
    
#     def __call__(self, num): #result = audi(when the vule is passed this will run) > makes it callable. Result is the 2nd obj
#         #when I want to use the object as callable meaning pass values.
#         vehicle_new = Vehicle()
#         vehicle_new.wheels = num
#         return vehicle_new
    
#     def __add__(self,other):
#         #when I want to add two objects
#         print("Two obj added")
#         vehicle_new = Vehicle(self.wheels+other.wheels,self.windows+other.windows)
#         return vehicle_new
    
#     def start(self):
#         print("The vihicle is now on.")

# toyota = Vehicle()
# audi = Vehicle()
# # audi.wheels = 4
# # print(audi)

# # result = audi(2) #result is an object, because __call__ is returning the vehicle_new obj.
# # print(result)

# tesla = toyota + audi

# print(tesla.wheels,tesla.windows)



# Implement __mul__ magic function

# class Car:
#     def __init__(self, wheel=4, window=4):
#         self.wheel = wheel
#         self.window = window
#     def __mul__(self,other):
#         return Car(self.wheel*other.wheel,self.window*other.window)


# toyota = Car()
# audi = Car()

# tesla = toyota*audi

# print(tesla.wheel,tesla.window)


'''Encapsulation'''

# cannot let user to manupulate the data.
        
# class Vehicle:
#     horn = "Beep Beep" 
#     def __init__(self,wheel,window):
#         self.__wheels = wheel #private variable
#         self.__windows = window
        
#     def start(self): 
#         print(self.__wheels) #only can be used in func and class
#         print("The vihicle is now on.")

#     def get_wheel(self): #getter
#         return self.__wheels

#     def set_wheel(self,num):
#         self.__wheels = num #setter


# toyota = Vehicle(4,4)
# audi = Vehicle(4,4)

# audi.start()

# #how to manipulate private variables
# #only can be accessed through functions
# print(audi.get_wheel())


'''Abstraction'''
'''it is not directly not supported in python'''
from abc import ABC,abstractmethod

class Vehicle(ABC):
    horn = "Beep Beep" 
    def __init__(self):
        self.wheels = 4 #private variable
        self.windows = 4
    
    @abstractmethod #meaning this is medatory to make it in other classes as well.
    #Tells the structure of the class.
    def start(self): 
        pass

class Toyota(Vehicle):
    def start(self):
        print('Car started.')
    def stop(self):
        print("Car stopped.")

mycar = Toyota()
