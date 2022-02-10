class Student:
    def __init__(self,first,last,age,id,cgpa):
        self.first = first
        self.last = last
        self.age = age
        self.id = id
        self.cgpa = cgpa

    def emailbuilder(self):
        return f'{self.first}.{self.last}@university.com'

    def math(self):
        return self.age*self.cgpa

class UndergradStudent():
    pass
student1 = Student("Mr","Tom",20,10,3.50)
print(student1.first,student1.last)
student2 = Student("Mr","Jerry",19,11,3.20)
print(student1.first,student1.last)

print(student1.emailbuilder())
print(student2.emailbuilder())
print(student1.math())