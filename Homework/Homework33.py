class Human:

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old'

class Student(Human):

    def __init__(self, first_name, last_name, age, gender, record_book):
        super().__init__(first_name, last_name, age, gender)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, record book: {self.record_book}'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        res = self.find_student(last_name)
        if res:
            self.group.remove(res)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        return f'Number:{self.number}\n{all_students} '



st1 = Student('Steve', 'Jobs', 30, 'Male', 'AN142')
st2 = Student('Liza', 'Taylor', 25, 'Female', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'

gr.delete_student('Taylor')
print(gr) # Only one student