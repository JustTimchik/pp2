class Parent:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def greet(self):
        return f"Hello, my name is {self.name} {self.last_name}."

class Child(Parent):
    def __init__(self, name, last_name, age):
        super().__init__(name, last_name)
        self.age = age

    def greet(self):
        return f"{super().greet()} I am {self.age} years old." # Override the greet method in the Child class to include the age information. It calls the parent class's greet method using super() and appends additional information about the child's age.

child_1 = Child("Alice", "Smith", 10)
print(child_1.greet())
