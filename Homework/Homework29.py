def generate_cube_numbers(end):
    num = 2
    while True:
        num_cube = num ** 3
        if num_cube < end:
            yield num_cube
            num += 1
        else:
            return

assert list(generate_cube_numbers(10)) == [8], 'поскольку оно меньше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 в кубе это 125, а оно уже больше 100'
print('OK')