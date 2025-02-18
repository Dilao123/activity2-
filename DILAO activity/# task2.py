# task2.py

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi sir, my name is {self.name}. I am {self.age} years old and I study {self.course}.")

student1 = Student("Angelo", 22, "Programmer")
student2 = Student("Aaron", 19, "Elictrical")
student3 = Student("Patrick", 18, "Scientist")


student1.introduce()
student2.introduce()
student3.introduce()