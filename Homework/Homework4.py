num_one = float(input('Введите первое число: \n'))
num_two = float(input('Введите второе число: \n'))
operation = int(input('Выберите номер операции , где: \n1 это (+) \n2 это (-) \n3 это (*) \n4 это (/) \n'))

if operation == 1:
    print('Сумма чисел равна', num_one + num_two)
elif operation == 2:
    print('Разность чисел равна', num_one - num_two)
elif operation == 3:
    print('Произведение чисел равно', num_one * num_two)
elif operation == 4 and num_two == 0:
    print('Операция невозможна , на ноль делить нельзя')
elif operation == 4:
    print('Частное чисел равно', num_one / num_two)
else:
    print('Неизвестная операция')