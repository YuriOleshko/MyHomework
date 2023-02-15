def add_one(lst):
    txt_num = ''
    for i in lst:
        txt_num += str(i)
    txt_num = str(int(txt_num) + 1)
    lst = [int(x) for x in txt_num]
    return lst

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9, 9]) == [1, 0, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")