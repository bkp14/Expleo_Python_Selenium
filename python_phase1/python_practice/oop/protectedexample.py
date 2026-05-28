class Student:
    def __init__(self, name):
        self._name = name   # protected variable


class College(Student):
    def show(self):
        print("Student name:", self._name)


c = College("Python")
c.show()