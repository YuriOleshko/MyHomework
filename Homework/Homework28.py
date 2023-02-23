def prime_generator(end):
    for i in range(end):
        sum = 0
        if i != 0 and i != 1:
            for x in range(2, (i//2)+1):
                if i % x == 0:
                    sum += 1
            if not sum:
                yield i

assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
print('OK')