'''
To install a library/package we can use "pip install <name>"
For example: pip install mysql-connect

it downloads from pypi.org

Library - 
Package -
Module - 

when building a package we my make many files that are only in our device. So, do it in Gooogle
collab.
install in collab - !pip install bntrans

'''


'''
For testing we have to use local ddvice. In collab we cannot do all the testing.
'''

'''#Testing in python'''

# >>> is used for doctest
# we also need to import doctest
#there is a command for doc text - python3 -m doctest package.py -v

# class Calc:
#     def __init__(self):
#         self.a = 2
#         self.b = 2
#     def add(self):
#         return self.a+self.b
#     '''
#     >>> Calc = Calc()
#     >>> Calc.add()
#     4

#     '''
    
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()


class Nums:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1+self.num2

def addition(result):
    print(result+6)

numbers = Nums(2,2)
re = addition(numbers.add())

