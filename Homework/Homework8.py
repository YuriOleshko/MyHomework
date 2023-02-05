lst = [1, 3, 5]
#lst = [6]
#lst = []
sum = 0
if len(lst):
    for i in range(0, len(lst), 2):
        sum += lst[i]
    print(sum * lst[-1])
else:
    print(0)