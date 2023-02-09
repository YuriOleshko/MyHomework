import keyword
import string

punkt = list(string.punctuation)
index = punkt.index('_')
punkt[index] = ' '
txt = input("Введите имя предпологаемой переменной: \n")
if not keyword.iskeyword(txt):
    if not txt[0].isnumeric():
        for i in txt:
            if i.isupper() or i in punkt:
                print("False")
                break
        else:
            print("True")
    else:
        print("False")
else:
    print("False")

