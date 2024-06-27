class Animal:
    def speak(self):
        pass

    def move(self):
        pass

class Dog:
    def __init__(self, animal):
        self.animal = animal

    def speak(self):
        self.animal.speak()

    def move(self):
        self.animal.move()


animal = Animal()
dog = Dog(animal)
dog.speak()
dog.move()