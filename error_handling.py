#syntex error is also know as persing error

try:
    x = int(input("Please enter a number: "))
    print(10/x)
except ValueError:
    print("Oops! That was no vaild number. Try again...")
except ZeroDivisionError:
    print("Opps! cannot devide by zero.")

#IF an error happens in project the entire program collapses.
#We use 'Try' in risky or expected fields.

try:
    x = int(input("Please enter a number: "))
    print(10/x)
except Exception as e:
    print("Oops! That was no vaild number. Try again...",e) #what if we don't know what error will get.


#as many times as needed exception
# is discuraged
# we can make custom errors using class. (Advance.)


#___________________________________
'''
    When a module is called
'''

#__name__

if __name__ =='__main__':
    pass #only the module script will run

#allows us to use it in other files without running it in this one.