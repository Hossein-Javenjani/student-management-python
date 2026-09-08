class Student:

    def __init__(self, name, age, field, average, skills):
        self.name = name
        self.age = age
        self.field = field
        self.average = average
        self.skills = skills

    def __str__(self):
        return f"name : {self.name}\nage : {self.age}\nfield : {self.field}\n\
average : {self.average}\nskills : { self.skills}\n"
