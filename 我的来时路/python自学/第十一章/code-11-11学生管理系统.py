class User(object):
    def __init__(self, name, age, gender, id_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.id_number = id_number

    def show(self):
        print("*" * 30)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("ID:", self.id_number)
        print("*" * 30)

class Student(User):
    def __init__(self,name,age,gender,id_number):
        super().__init__(name,age,gender,id_number)

    def show(self):
        super().show()

class Teacher(User):
    def __init__(self,name,age,gender,id_number,dao,cla):
        super().__init__(name,age,gender,id_number)
        self.dao = dao
        self.cla = cla

    def show(self):
        super().show()
        print("tutor or not:",self.dao)
        print("which class:")
        for i in self.cla:
            print(i)
        print("*" * 30)

class Class(object):
    def __init__(self,name,id_number,teacher,students):
        self.name = name
        self.id_number = id_number
        self.teacher = teacher
        self.students = students

    def show(self):
        print("*"*15,"班级信息","*"*15)
        print("class:",self.name)
        print("id_number:",self.id_number)
        print("teacher:",self.teacher.name)
        print("students:")
        for i in self.students:
            print(i.name)
        print("*" * 15, "班级信息", "*" * 15)

    def add_student(self,student):
        self.students.append(student)

    def sub_student(self,student):
        self.students.remove(student)

class Course(object):
    def __init__(self,name,id_number,teacher,students,type,number):
        self.name = name
        self.id_number = id_number
        self.students = students
        self.teacher = teacher
        self.type = type
        self.number = number

    def show(self):
        print("*"*15,"课程信息","*"*15)
        print("course:",self.name)
        print("id_number:",self.id_number)
        print("teacher:",self.teacher.name)
        print("students:")
        for i in self.students:
            print(i.name)
        print("*" * 15, "课程信息", "*" * 15)


mia = Student(name="Mia",age=12,gender="F",id_number="123456")
mia.show()
John = Teacher(name="John",age=32,gender="M",id_number="654321",dao="true",cla = ["class1","class2"])
John.show()
class3 = Class(name="计算机二班",id_number="123456",teacher = John,students=[mia])
class3.show()
class4 = Class("计算机二班",id_number="123456",teacher = John,students=[])
class3.sub_student(mia)
class4.add_student(mia)
class4.show()
class3.show()
python = Course("Python",1,John,[mia],"必修课",6)
python.show()


