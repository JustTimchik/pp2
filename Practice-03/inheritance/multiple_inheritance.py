class Support_brawler: # This class represents a support brawler that can heal other brawlers.
    def __init__(self, name, health, heal_amount):
        self.name = name
        self.health = health
        self.heal_amount = heal_amount

    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Heal Amount: {self.heal_amount}")
    def heal(self, target):
        target.health += self.heal_amount
        print(f"{self.name} heals {target.name} for {self.heal_amount} health points.")

class damage_brawler: # This class represents a damage brawler that can attack other brawlers.
    def __init__(self, name, health, damage_amount):
        self.name = name
        self.health = health
        self.damage_amount = damage_amount

    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Damage Amount: {self.damage_amount}")
    def attack(self, target):
        target.health -= self.damage_amount
        print(f"{self.name} attacks {target.name} for {self.damage_amount} damage points.")

class Hybrid_brawler(Support_brawler, damage_brawler): # This class represents a hybrid brawler that can both heal and attack other brawlers. It inherits from both the Support_brawler and damage_brawler classes.
    def __init__(self, name, health, heal_amount, damage_amount):
        Support_brawler.__init__(self, name, health, heal_amount)
        damage_brawler.__init__(self, name, health, damage_amount)

Byron = Hybrid_brawler("Byron", 100, 15, 25)
Shelly = damage_brawler("Shelly", 100, 20)
Byron.display_info()
Shelly.display_info()
Byron.attack(Shelly) # Byron attacks Shelly, using the attack method from the damage_brawler class
Shelly.display_info()
Byron.heal(Shelly) # Byron heals Shelly, using the heal method from the Support_brawler class
Shelly.display_info()