# Question 2,3
from abc import ABC, abstractmethod
import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        # Your Code Here
        return torch.exp(x) / torch.exp(x).sum()
        # End Code Here


data = torch.Tensor([5, 2, 4])
my_softmax = MySoftmax()
output = my_softmax(data)
assert round(output[-1].item(), 2) == 0.26
print(output)

data2 = torch.Tensor([1, 2, 300000000])
my_softmax2 = MySoftmax()
output2 = my_softmax2(data2)
assert round(output2[0].item(), 2) == 0.0
print(output2)

# Question 4


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition


data3 = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output3 = softmax_stable(data3)
assert round(output3[-1].item(), 2) == 0.67
print(output3)


# Question 5,6,7


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        # Your Code Here
        super().__init__(name, yob)
        self.grade = grade
        # End Code Here

    def describe(self):
        # Your Code Here
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        # Your Code Here
        super().__init__(name, yob)
        self.subject = subject
    # End Code Here

    def describe(self):  # Your Code Here
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.subject}")
    # End Code Here


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        # Your Code Here
        super().__init__(name, yob)
        self.specialist = specialist
    # End Code Here

    def describe(self):  # Your Code Here
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.specialist}")

    # End Code Here
student1 = Student(name="studentZ2023", yob=2011, grade="6")
assert student1._yob == 2011
student1.describe()
teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
assert teacher1._yob == 1991
teacher1.describe()

doctor1 = Doctor(name="doctorZ2023", yob=1981, specialist="Endocrinologists")
assert doctor1._yob == 1981
doctor1.describe()
# Question 8


class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__listPeople = list()

    def add_person(self, person: Person):
        self.__listPeople.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__listPeople:
            p.describe()

    def count_doctor(self):
        # Your Code Here
        return sum(isinstance(person, Doctor) for person in self.__listPeople)

        # End Code Here
student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
print(ward1.count_doctor())

# Question 9,10


class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        # Your Code Here
        if self.is_full():
            print("Stack is full")
            return False
        self.__stack.append(value)
        # End Code Here

    def top(self):
        # Your Code Here
        return self.__stack[-1]

        # End Code Here
stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print(stack1.is_full())
print(stack1.top())

# Question 11,12


class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def isEmpty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.__queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            return False
        self.__queue.append(value)

    def front(self):
        if self.isEmpty():
            return None
        return self.__queue[0]


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
