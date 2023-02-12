def second_index(txt, txt_search):
    x = txt.find(txt_search, txt.find(txt_search) + 1)
    if x == -1:
        x = None
        return x
    else:
        return x

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") == None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')