start = 0
end = 10
step = 2
for i in range(start,end,step):
    if i == 8:
        break
    print(i)
else: #else can be used with for loop as well.
    print('Done')
# if only loop finishes compeletly, will be done in continue but not in break.
# if the condition is out of range else will run. if == 60

