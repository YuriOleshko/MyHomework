sec = int(input('Введите количество секунд: '))

if sec >= 0 and sec <= 8639999:
    day = sec//60//60//24
    if day % 10 == 1 and day % 100 != 11:
        daytxt = 'день,'
    elif 2 <= day % 10 <= 4:
        daytxt = 'дня,'
    else:
        daytxt = 'дней,'

    print(day, daytxt , f'{sec//60//60%24:02}:{sec//60%60:02}:{sec%60:02}')
else:
    print('Не корректное значение')