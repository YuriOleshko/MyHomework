import string

def is_palindrome(txt):
    txt = txt.lower()
    txt = "".join(i for i in txt if i not in string.punctuation and i not in ' ')
    txt_one = txt[::-1]
    if txt == txt_one:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
print("ОК")