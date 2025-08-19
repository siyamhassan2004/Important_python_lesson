# text = "12,20,54,89"

# num = text.split(",")
# num2 = []
# for item in num:
#     num2.append(int(item))
# print(num2)


# text = "(31,2),(10,23),(35,19)"
# data = text.split(",")
# my_lst = []
# temp = []
# for item in data:
#     if item[0] == "(":
#         temp.append(int(item[1:]))
#     else:
#         temp.append(int(item[:-1]))
#         my_lst.append(tuple(temp))
#         temp = []
# print(my_lst)


# text = "name: Eshikhon, age: 28, address: Dhaka"

# data = text.split(",")
# my_dic = {}

# for pair in data:
#     temp = pair.split(":")
#     my_dic[temp[0].strip()] = temp[1].strip()

# print( my_dic)

email = "abc@gmail.com,nasim123@gmail.com,1shikhon@.com"
valid = ['gmail.com']
data = email.split(',')

for item in data:
    temp = item.split("@")
    if temp[1] in valid:
        print(item)