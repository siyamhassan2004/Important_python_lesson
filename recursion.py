
# #a function that acts like a loop

# def Greeting(age):
#     if age == 20:
#         return #not this one
#     #'return' this return is the end of the goal for any func.
#     print(age) #normal output
#     Greeting(age+1)
#     print(age) #reverse output

# x = Greeting(13)



def is_prime(x):
    division_count = 0
    for i in range(2,x):
        if x % i == 0:
            division_count+=1
    return division_count



def prime_printer(start,end):
    for i in range(start,end):
        if i == 1:
            continue
        count = is_prime(i)
        if count == 0:
            print(i,end=",")

prime_printer(1,21)