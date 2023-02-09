num = int(input('Введите число больше 0: '))
lst = []
if num > 0:
    while num > 9:
        lst = list(str(num))
        num = 1
        for i in lst:
            num = int(num) * int(i)
    print(num)