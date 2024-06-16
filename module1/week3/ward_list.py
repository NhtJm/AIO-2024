class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(
            f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        return sum(isinstance(person, Doctor) for person in self.people)

    def sort_age(self):
        self.people.sort(key=lambda x: x.yob,reverse=True)

    def compute_average(self):
        teachers = [
            person for person in self.people if isinstance(person, Teacher)]
        return sum([teacher.yob for teacher in teachers]) / len(teachers)


student1 = Student(name=" studentA ", yob=2010, grade="7")
student1.describe()
# output >> Student - Name : studentA - YoB : 2010 - Grade : 7
teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher1.describe()
# output >> Teacher - Name : teacherA - YoB : 1969 - Subject : Math

doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
doctor1.describe()
# output >> Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists


teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name=" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()
# output >> Ward Name: Ward1
# Student - Name: studentA - YoB: 2010 - Grade: 7
# Teacher - Name: teacherA - YoB: 1969 - Subject: Math
# Teacher - Name: teacherB - YoB: 1995 - Subject: History
# Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists
# Doctor - Name: doctorB - YoB: 1975 - Specialist: Cardiologists
print(f"\nNumber of doctors : {ward1.count_doctor()}")

print("\nAfter sorting Age of Ward1 people ")
ward1.sort_age()
ward1.describe()

print(f"\nAverage year of birth ( teachers ): {ward1 . compute_average()}")
