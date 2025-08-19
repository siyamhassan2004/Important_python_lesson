'''
Function:
    * To not repeat code over and over.
    * 1st rule of coding keep your code DRY (Don't Repeat Yourself)
    * def -> define VariableName(): 
        fucntion
'''

# def Greetings():
#     print("Good morning")
#     print("Good noon")
#     print("Good evening")
#     print("Good night")

# Greetings() #a function needs to be called.
# # is there no time delay? What is happening under the hood?
# # does it cache? Does it makes it slow?

'''
Python interpreter see the keyword "def" keep the name of the func in cache.
when called goes to the func and runs what's inside.
'''

# def Greetings(name,age):
#     print(f'Nice to meet you {name}')
#     print(f'Your age is {age}')

# Greetings("Siaym","20")

# # can you wrap in int(age)? Answer: NO

def Age(age):
    return age+1 #only if we want to store a value in a variable.

x = Age(12)
print(x)