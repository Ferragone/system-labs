class Person:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def is_adult(self):
        return self.age >= 18

    def calculate_score(self, score1, score2, score3, score4, score5):
        total_score = sum([score1, score2, score3, score4, score5])
        return total_score

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Height:", self.height)
        print("Weight:", self.weight)
        print("Total Score:", self.calculate_score(85, 90, 75, 88, 92))
        print("Adult:", self.is_adult())


person = Person("John", 25, "Male", 175, 70)
person.print_details()