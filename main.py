class Animal:
    def __init__(self, color, age, name, energy):
        self.color = color
        self.age = age
        self.name = name
        self.energy = energy

    def information(self):
        return f"Color: {self.color}, age: {self.age}, name: {self.name}, energy: {self.energy}"
    
    def change_name(self, new_name):
        self.name = new_name

    def change_color(self, new_color):
        self.color = new_color

    def grow(self, age):
        self.age = age

    def feed(self):
        self.energy *= 1.5


class Cat(Animal):
    def __init__(self):
        super().__init__("Grey", 2, "Tom", 5)

    def speek(self):
        return "Meow"
    

class Dog(Animal):
    def __init__(self):
        super().__init__("Brown", 3, "Bob", 6)

    def speek(self):
        return "Vov"
    


dog = Dog()

print(dog.information())
dog.change_name("Jerry")
dog.change_color("Red")
dog.feed()
dog.grow(4)
print(dog.information())
print(dog.speek())

cat = Cat()

print(cat.information())
cat.change_name("Jerry")
cat.change_color("Red")
cat.feed()
cat.grow(4)
print(cat.information())
print(cat.speek())
