#create class name Animal
class Animal:
    def __init__(self, name):
        self.name = name
        self.species = "Unknown from Animal class"
        print("Animal class constructor called for", self.name)

    def make_sound(self):
        print("Some generic animal sound")



# animal = Animal("Generic Animal")
# print(animal.name)  # Output: Generic Animal
# animal.make_sound()  # Output: Some generic animal sound


class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.breed = "Unknown from Dog class"
        self.age = 0
        super().__init__(name)  # Call the constructor of the parent class

    def make_sound1(self):
        super().make_sound()  # Call the make_sound method from the parent class
        print("Woof!")

dog = Dog("Buddy")
print(dog.name)  # Output: Buddy
print(dog.breed)  # Output: Unknown from Dog class
print(dog.species)  # Output: Unknown from Animal class
print(dog.age)  # Output: 0
dog.make_sound1()  # Output: Woof!
dog.make_sound()  # Output: Some generic animal sound (inherited from the Animal class)



