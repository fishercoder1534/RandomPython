# class names are always capitalized while function names are always lowercase
class Sample:
    pass


x = Sample()
print(type(x))


class Dog():
    # CLASS OBJECT ATTRIBUTES
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


my_dog = Dog("Lab", "Sammy")
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)


class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


my_circle = Circle(3)
print(my_circle.radius)
print(my_circle.area())
my_circle.set_radius(5)
print(my_circle.radius)
print(my_circle.area())


class Animal():

    def __init__(self):
        print("Animal created!")

    def who_am_I(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Cat(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Cat created.")

    def meow(self):
        print("Meow")


my_cat = Cat()
print(my_cat.eat())


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  # this is similar to toString() method in Java objects
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __del__(self):
        print("A book is destroyed!")

    # methods that start with double underscores are special methods with a class/object in Python


my_book = Book("Python is fun!", "Steve", 340)
print(my_book)
del my_book
