class Human:
    def __init__(self, name, age, wage):
        self.name = name
        self._age = age
        self.__wage = wage
    def introduce(self):
        print(f"Hi, I'm {self.name}")

shubham = Human("Shubham", 34, 100)
shubham.introduce()
print(shubham.name)
print(shubham._age)
try:
    print(shubham.__wage)
except:
    print("Can't access __wage")

class Student(Human):
    def __init__(self, name, age, school, wage=0):
        super().__init__(name, age, wage)
        self.school = school
    def introduce(self):
        print(f"Hi, I'm {self.name} and I study at {self.school}.")

shubham = Student("Shubham", 34, 'USF')
shubham.introduce()

class Baby(Human):
    def __init__(self, name, age, month, wage=0):
        super().__init__(name, age, wage)
        self.month = month

    def introduce(self):
        print("Goo Goo Gaga")

    def print_sleep_hours(self):
        if self.month < 1:
            hours = 16
        elif self.month <= 6:
            hours = 15
        else:
            hours = 14
        print(f"{self.name} sleeps {hours} hours a day.")

b = Baby("Nora", 0, 3)
b.introduce()
b.print_sleep_hours()


