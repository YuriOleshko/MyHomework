lst = [12, 3, 4, 10]
#lst = [1]
#lst = []
#lst = [12, 3, 4, 10, 8]
lst_one = []
lst_new = []
lst_one.append(lst[len(lst)-1:len(lst)])
lst_new.extend(lst_one[0])
lst_new += lst[:len(lst)-1]
print(lst_new)
