# lst = [1,3,5,5]

# my_iter = iter(lst) #has no idex
# print(type(my_iter)) #only knows 1
# print(next(my_iter)) #only knows 3
# print(next(my_iter)) #only knows 5

'''Doesn't keep all the elements of a list. Uses less memory.
When to use?
> when we need to access all the elements

Let's say you want to access one of the elements iterator is not good in that case.

'''


# def my_generator():
#     yield 10
#     yield 12
#     yield 199
#     yield 200

# my_gen = my_generator()
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

'''With generator we generate an iterator. We use yield for this.'''


#denerator
# when we decorate func.

# def my_decorator(my_func):
#     def wrapper():
#         print("Before the function.")
#         my_func() #the function
#         print("After")
#     return wrapper

# @my_decorator
# def greetings():
#     print("Good morning.")


# greetings()

'''Excel file reading using python'''
import pandas as pd
from openpyxl.styles import colors
# df = pd.read_csv('new.csv')

# # print(df.head())

# df.iloc[0,0] = 'Mohammad'

# df.to_csv("Output.csv")

df = pd.read_excel('sample.xlsx')
ft = colors.BLUE
df.iloc[1,1] = 560
print(df.head())

