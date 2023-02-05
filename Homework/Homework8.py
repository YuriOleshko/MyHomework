lst = [1, 3, 5]
#lst = [6]
#lst = []
sum = 0
i = 0
if len(lst):
    while i < len(lst):
        x = lst[i]
        sum += x
        i += 2
    print(sum * lst[-1])
else:
    print(0)