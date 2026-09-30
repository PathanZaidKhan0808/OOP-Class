class Student:
    def __init__(self, r, n, mar, add):
        self.roll = r
        self.name = n
        self.marks = mar
        self.address = add

    def show_student(self):
        print("Student Information")
        print("Roll No :", self.roll)
        print("Name :", self.name)
        print("Marks :", self.marks)
        print("Address :", self.address)


class Teacher:
    def __init__(self, n, sal, dept, add):
        self.name = n
        self.salary = sal
        self.department = dept
        self.address = add

    def show_teacher(self):
        print("Teacher Information")
        print("Name :", self.name)
        print("Salary :", self.salary)
        print("Department :", self.department)
        print("Address :", self.address)


# Object Student
student1 = Student(101, "Zaid", 83, "Pune")
student1.show_student()

print()

# Object Teacher
teacher1 = Teacher("Atul Sir", 75000, "Data Analytics / Core Python", "Pune")
teacher1.show_teacher()