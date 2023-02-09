import string

txt = input('Введите строку , а я преобразую её в hashtag: ')
txt = txt.title()
punkt = list(string.punctuation)
punkt.append(' ')
lst = []
for i in txt:
    if not i in punkt:
        lst.append(i)
if len(lst) > 140:
    lst = lst[:139]
    #закладываю 139 символов так как будет ещё один символ, сам хештег
txt = "".join(lst)
print('#' + txt)