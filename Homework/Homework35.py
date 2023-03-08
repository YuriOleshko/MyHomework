class GroupOverflowError(Exception):
    pass

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
        if len(self.group) >= 10:
            raise GroupOverflowError('Cannot add more than 10 students to the group.')
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


students = []
gr = Group('PD1')
st1 = Student('Steve', 'Jobs', 30, 'Male', 'AN142')
st2 = Student('Liza', 'Taylor', 25, 'Female', 'AN145')
st3 = Student('Liza', 'Taylor', 25, 'Female', 'AN145')
st4 = Student('Liza', 'Taylor', 25, 'Female', 'AN145')
st5 = Student('Liza', 'Taylor', 25, 'Female', 'AN145')
st6 = Student('Liza', 'Taylor', 25, 'Female', 'AN145')
st7 = Student('Liza', 'Taylor', 25, 'Female', 'AN145')
st8 = Student('Liza', 'Taylor', 25, 'Female', 'AN145')
st9 = Student('Liza', 'Taylor', 25, 'Female', 'AN145')
st10 = Student('Liza', 'Taylor', 25, 'Female', 'AN145')
st11 = Student('Liza', 'Taylor', 25, 'Female', 'AN145')
students.append(st1)
students.append(st2)
students.append(st3)
students.append(st4)
students.append(st5)
students.append(st6)
students.append(st7)
students.append(st8)
students.append(st9)
students.append(st10)
students.append(st11)

for student in students:
    try:
        gr.add_student(student)
    except GroupOverflowError as e:
        print(f"Failed to add student {e}")

print(gr)




