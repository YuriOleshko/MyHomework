lst = [0, 1, 0, 3, 12]
#lst = [0]
#lst = [1, 0, 3, 0, 0, 0, 5]
#lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
lst1 = []
lst1 = [i for i in lst if i]
lst = [i for i in lst if i == 0]
print(lst1 + lst)