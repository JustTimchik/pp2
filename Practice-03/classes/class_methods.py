class Brawler: # Define a class named Brawler
    def __init__(self, name, health, damage): #assigning attributes to the Brawler class
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, other_brawler):  # Define a method named attack that takes self and another Brawler object as a parameter
        other_brawler.health -= self.damage # Subtract the damage of the attacking Brawler from the health of the other Brawler
        print(f"{self.name} attacks {other_brawler.name} for {self.damage} damage!")

brawler1 = Brawler("Shelly", 100, 20)
brawler2 = Brawler("Colt", 100, 15)

print(f"{brawler1.name} has {brawler1.health} health and {brawler1.damage} damage.")
print(f"{brawler2.name} has {brawler2.health} health and {brawler2.damage} damage.")
brawler1.attack(brawler2)
print(f"{brawler2.name} has {brawler2.health} health left.")
