class Fruit:
    def __init__(fruit_itself, color, taste): # The __init__ method is a special method in Python classes that is called when an object is created. It is used to initialize the attributes of the object.
        fruit_itself.color = color  # assign the color parameter to the color attribute of the object, which is basically the fruit_itself 
        fruit_itself.taste = taste # assign the taste parameter to the taste attribute of the object, which is basically the fruit_itself

    def description(fruit_itself):
        print(f"This is a {fruit_itself.color} fruit that tastes {fruit_itself.taste}.")

apple = Fruit("red", "sweet") # creating an object named apple from the Fruit class
apple.description()