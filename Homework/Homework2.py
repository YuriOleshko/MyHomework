num = int(input('Введите 4-х значное число: '))
inference = num % 10
after = num // 10
print(inference)
inference = after % 10
after = after // 10
print(inference)
inference = after % 10
after = after // 10
print(inference)
inference = after % 10
after = after // 10
print(inference)