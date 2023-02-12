import random

def common_elements():
    lst_one = []
    for i in range(100):
        x = random.randint(1, 100)
        if x % 3 == 0:
            lst_one.append(x)
    lst_two = []
    for i in range(100):
        x = random.randint(1, 100)
        if x % 5 == 0:
            lst_two.append(x)
    num_first = set(lst_one)
    num_second = set(lst_two)
    return (num_first & num_second)
