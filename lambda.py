# s = lambda lst: [x**2 for x in lst]

# print(s([3,7]))


# f = lambda lst: [2* x **2 + 2*x +7 for x in lst]
# print(f([9]))

# lst = [1,2,3,4,5,6]
# result = [item**2 for item in lst] #[Expression, for loop]
# print(result)

# lst = [1,2,3,4,5,5]
# my_set = {i for i in lst}
# print(my_set)

key = ['name','age','gender']
value = ['eshikhon',20,'male']

my_dict = {key[i]: value[i] for i in range(len(key))}
print(my_dict)