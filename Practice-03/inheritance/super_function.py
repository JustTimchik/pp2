class Parent:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def greet(self):
        return f"Hello, my name is {self.name} {self.last_name}."

class Child(Parent):
    def __init__(self, name, last_name, age):
        super().__init__(name, last_name) # call the parent class's __init__ method to initialize the name and last_name attributes (No need to repeat the code for initializing these attributes)
        self.age = age # initialize the age attribute specific to the Child class

child_1 = Child("Alice", "Smith", 10)
print(child_1.greet())