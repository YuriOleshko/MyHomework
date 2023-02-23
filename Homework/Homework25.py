def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    for i in range(end):
        yield begin
        begin = pow(begin)

assert list(some_gen(2, 4, pow)) == [2, 4, 16, 256], 'Test1'
print('OK')