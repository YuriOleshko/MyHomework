lst = [1, 2, 3, 4, 5, 6]
#lst = [1, 2, 3]
#lst = [1, 2, 3, 4, 5]
#lst = [1]
#lst = []
lst_one = []
long_lst = len(lst) + 1
lst_one.append(lst[0 : int(long_lst / 2)])
lst_one.append(lst[int(long_lst / 2) : long_lst - 1])
print(lst_one)
