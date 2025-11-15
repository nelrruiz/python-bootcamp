class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        return f"Hello, I am {self.first_name} {self.last_name}!"

class Student(Person):
    def introduce(self):
        return super().introduce() + " " + f"Hello, I am a student."

student = Student("Jackie", "Chan")
print(student.introduce())

############### alternate
from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    
    def introduce(self):
        return f"Hello, I am {self.first_name} {self.last_name}!"

@dataclass
class Student(Person):
    student: int
    
    def introduce(self):
        return super().introduce() + " " + f"Hello, I am a student."