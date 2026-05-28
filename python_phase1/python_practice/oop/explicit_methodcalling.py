class teammember:

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def display(self):
        print(f"name: {self.name}, uid: {self.uid}")


class worker(teammember):

    def __init__(self, pay, pos):
        self.pay = pay
        self.pos = pos

    def display(self):
        super().display()
        print(f"pay: {self.pay}, pos: {self.pos}")


class teamleader(worker,teammember):

    def __init__(self, name, uid, pay, pos, exp):

        teammember.__init__(self, name, uid)
        worker.__init__(self, pay, pos)

        self.exp = exp

    def display(self):
        super().display()
       
        print(f"exp: {self.exp}")


ob = teamleader("kp", 20, 20000, "scrum", 12)

ob.display()