class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}, gender: {self.gender}, age: {self.age}'
class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender,age, first_name, last_name)
        self.record_book = record_book
    def __str__(self):
        return super().__str__() + f', record_book: {self.record_book}\n'
class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
    def add_student(self, student):
        self.group.add(student)
    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None
    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student)
        return f'Number:{self.number}\n {all_students} '
