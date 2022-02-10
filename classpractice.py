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

    def printing(self):
        print(f'''First Name: {self.first}
Last Name: {self.last}
Age: {self.age}
ID: {self.id}
CGPA: {self.cgpa}''')


class UniStudent(Student):
    def __init__(self,first,last,age,id,cgpa,uni):
        super().__init__(first,last,age,id,cgpa)
        self.uni = uni

    def view(self):
        super().printing()
        print(self.uni)


class CollegeStudent(Student):
    def __init__(self,first,last,age,id,cgpa):
        super().__init__(first,last,age,id,cgpa)


student1 = UniStudent("Mr","Tom",20,5,3.20,"BUET")
student1.view()

# student1 = CollegeStudent("Mr","Jerry",19,5,3.3)
# student1.printing()


# student1 = Student("Mr","Tom",20,10,3.50)
# print(student1.first,student1.last)
# student2 = Student("Mr","Jerry",19,11,3.20)
# print(student1.first,student1.last)
#
# print(student1.emailbuilder())
# print(student2.emailbuilder())
# print(student1.math())
