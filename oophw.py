class College:
    def __init__(self, n, stu, tea, add):
        self.name = n
        self.student = stu
        self.teacher = tea
        self.address = add


class Student:
    def __init__(self, r, n, mar, add):
        self.roll = r
        self.name = n
        self.marks = mar
        self.address = add


class Teacher:
    def __init__(self, n, sal, dept, add):
        self.name = n
        self.salary = sal
        self.department = dept
        self.address = add


class Address:
    def __init__(self, c, p):
        self.city = c
        self.pin = p

address1 = Address("Pune", 411038)
address_stu = Address("Pune", 411007)
address_college = Address("Karve Nagar Pune", 411411)

teacher1 = Teacher("Atul Sir", 75000, "Python", address1)

student1 = Student(21, "Zaid", 83, address_stu)

college1 = College("The Kiran Academy", student1, teacher1, address_college)

# Student information
print("Student Information")
print(college1.student.roll)
print(college1.student.name)
print(college1.student.marks)
print(college1.student.address.city)
print(college1.student.address.pin)


# Teacher information
print("Teacher Information")
print(college1.teacher.name)
print(college1.teacher.salary)
print(college1.teacher.department)
print(college1.teacher.address.city)
print(college1.teacher.address.pin)


# College information
print("College Information")
print(college1.name)
print(college1.address.city)
print(college1.address.pin)
