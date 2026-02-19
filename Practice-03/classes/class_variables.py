class Fruit:
    def __init__(self, color, taste):
        self.color = color
        self.taste = taste
Fruit.taste = "sweet" #assigning a default variable
Fruit.shape = "round" #assigning a default variable

apple = Fruit("red", "sweet")
lime= Fruit("green", "sour")

print(f"{apple.color} apple tastes {apple.taste} and is {apple.shape}.")
print(f"{lime.color} lime tastes {lime.taste} and is {lime.shape}.")
