def correct_sentence(txt):
    txt = txt.capitalize()
    if  not '.' in txt:
        lst = list(txt)
        lst.append('.')
        txt = "".join(lst)
    return txt

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings, friends") == "Greetings, friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')