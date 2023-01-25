num = int(input('Введите 5-ти значное число: '))
inference = num % 10
after = num // 10
last_num = after % 10
after = after // 10
inference = inference * 10 + last_num
last_num = after % 10
after = after // 10
inference = inference * 10 + last_num
last_num = after % 10
after = after // 10
inference = inference * 10 + last_num
last_num = after % 10
after = after // 10
inference = inference * 10 + last_num
print(inference)

