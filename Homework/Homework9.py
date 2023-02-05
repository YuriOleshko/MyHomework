import random
lst = [random.randint(0, 9) for i in range(random.randint(3, 10))]
print(lst)
lst1 = []
lst1.append(lst[0])
lst1.append(lst[2])
lst1.append(lst[-2])
print(lst1)