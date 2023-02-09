import string

lett = list(string.ascii_letters)
txt = list(input('Ведите две буквы через дефис: '))
lst = lett[lett.index(txt[0]):lett.index(txt[2]) + 1]
txt1 = "".join(lst)
print(txt1)