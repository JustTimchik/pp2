class Fruit: #parent class
    def __init__(self, name, color):
        self.name = name #parent class attribute
        self.color = color #parent class attribute

    def describe(self): #parent class method
        return f"{self.name} is {self.color}."

class Apple(Fruit): #child class that inherits from Fruit
    pass # nothing. an empty class that only inherits everything from the parent class

red_apple = Apple("red apple", "red") # creating an instance of the Apple class, which has the same attributes as the Fruit class
print(red_apple.describe()) #the same with a method
