num = int(input('Введите 4-х значное число: '))
inference = num // 1000
after = num % 1000
print(inference)
inference = after // 100
after = after % 100
print(inference)
inference = after // 10
after = after % 10
print(inference)
print(after)
