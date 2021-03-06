class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def print_pet(self):
        print("name: " + self.name, "\n"
              "gender: " + self.gender, "\n"
              "ages: " + str(self.age))