from student import Student

class StudentManager:

    def __init__(self):
        self.students = []

    def get_valid_float(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number!")

    def add_stu(self):
        name = input("inter name :")
        average = self.get_valid_float("inter average : ")
        try:
            age = int(input("inter age :"))
        except ValueError:
            age = int(input("age must be a int number : "))
        field = input("inter field :")
        """try:
            average = float(input("inter average :"))
        except ValueError:
            average = float(input("average must be a float number : "))"""
        try:
            number_of_skills = int(input("how many skills do you have ? "))
        except ValueError:
            number_of_skills = int(input("number of skills must be a int number : "))
        skills = []
        for i in range(1, number_of_skills + 1):
            skills.append(input(f"inter skill {i}: "))
        student = Student(name, age, field, average, skills)
        self.students.append(student)
        print("student added successfully !")

    def show_stu(self):
        if len(self.students) == 0:
            print("no student !")
        else:
            for number, info in enumerate(self.students, start=1):
                print(f"student {number} : \n{info}")
                print("=" * 20)

    def search(self):

        sch = input("search name : ").strip().lower()
        found = False
        for info in self.students:
            if sch == info.name.lower():
                print(f"this student found :\n{info}")
                found = True
                break
        if not found:
            print("student not found !")

    def delete(self):
        delete = input("inter name : ").strip().lower()
        found = False
        for info in self.students:
            if delete == info.name.lower():
                self.students.remove(info)
                print("student deleted successfully !")
                found = True
                break
        if not found:
            print("The student is not on this list !")

    def edit(self):
        edit_name_stu = (
            input("Whose information do you want to edit ? ").strip().lower()
        )
        found = False
        for info in self.students:
            if edit_name_stu == info.name.lower():
                info.name = input("inter new name : ")
                info.age = int(input("inter new age : "))
                info.field = input("inter new field : ")
                info.average = float(input("inter new average : "))
                num_of_skills = int(input("how many skills do you have ?"))
                info.skills = []
                for i in range(1, num_of_skills + 1):
                    info.skills.append(input(f"inter skill {i} : "))
                print("update seccessfully !")
                found = True
                return
        if not found:
            print("The student is not on this list !")

    def save(self):
        with open("info.txt", "w") as info_file:
            for info in self.students:
                info_file.write(f"{info}\n{'=' * 20}\n")
            print("Data saved successfully!")

    def load(self):
        with open("info.txt", "r") as info_file:
            return print(info_file.read())
