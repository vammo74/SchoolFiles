# rpg-game.py
# 3 moves Hard, finesse, stophit
#
from random import randint


class Warrior:
    def __init__(self, name, strength, agility, stamina, intellect, weapon):
        total_stats = strength + agility + stamina + intellect
        self.name = name
        self.strength = strength
        self.agility = agility
        self.stamina = stamina
        self.intellect = intellect
        self.weapon = weapon
        self.wounds = 0

        self.initial_stats = [strength, agility, stamina, intellect]

        self.initial_hitpoints = (self.strength * 5 + self.intellect) * self.stamina

        self.evasion = (self.agility + self.intellect) / total_stats
        self.hitpoints = 0

    def getUpdate(self, flag):
        if self.stamina > 3:
            if flag == "deep":
                self.stamina = self.stamina - 1
                self.agility = self.agility - 1
                self.strength = self.strength - 1
            self.stamina = self.stamina - 1
        self.hitpoints = (
            self.strength * 5 + self.intellect
        ) * self.stamina - self.wounds
        return 0


Mike = Warrior("Mike", 35, 20, 35, 10, "broadsword")
Vidar = Warrior("Vidar", 20, 35, 35, 10, "crossbow")


print(Mike.initial_hitpoints)
print(Mike.evasion)

print(Vidar.initial_hitpoints)
print(Vidar.evasion)

# game
#

# choose the starter
if Mike.weapon == "crossbow" and Vidar.weapon == "crossbow":
    warriors = [Mike, Vidar]
    x = randint(0, 1)
    first = warriors[x]
    second = warriors[abs(x - 1)]
elif Mike.weapon == "crossbow" and Vidar.weapon != "crossbow":
    first = Mike
    second = Vidar
elif Mike.weapon != "crossbow" and Vidar.weapon == "crossbow":
    first = Vidar
    second = Mike
else:
    warriors = [Mike, Vidar]
    x = randint(0, 1)
    first = warriors[x]
    second = warriors[abs(x - 1)]

print(first.name)


x = 0
while x < 3:
    x += 1
