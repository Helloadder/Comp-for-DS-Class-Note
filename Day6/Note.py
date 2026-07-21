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