#bubble sort
#selection sort
#insertion sort

'''
Buble sort

'''

num = [3, 1, 2]

for j in range(len(num)):

    count = 1
    for i in range(len(num)-1):
        if num[i]>num[i+1]:

            count+=1
            temp = num[i]
            num[i] = num[i+1]
            num[i+1] = temp


print(num,count)