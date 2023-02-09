import keyword
import string

punkt = string.punctuation
punkt1 = punkt.replace('_', ' ')
txt = input("Введите имя предпологаемой переменной: \n")
if not keyword.iskeyword(txt):
    if not txt[0].isnumeric():
        for i in txt:
            if i.isupper() or i in punkt1:
                print("False")
                break
        else:
            print("True")
    else:
        print("False")
else:
    print("False")

