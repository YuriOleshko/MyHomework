mark = True
while mark:
    num_one = float(input('Введите первое число: '))
    num_two = float(input('Введите второе число: '))
    operation = input('Выберите операцию: ')

    if operation == '+':
        print('Сумма чисел равна', num_one + num_two)
    elif operation == '-':
        print('Разность чисел равна', num_one - num_two)
    elif operation == '*':
        print('Произведение чисел равно', num_one * num_two)
    elif operation == '/' and num_two == 0:
        print('Операция невозможна , на ноль делить нельзя')
    elif operation == '/':
        print('Частное чисел равно', num_one / num_two)
    else:
        print('Неизвестная операция')

    str = input('Если Вы хотите продолжить введите "yes": ')
    str = str.lower()
    if str == 'yes':
        mark = True
    else:
        mark = False