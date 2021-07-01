# rpg-game.py

class Warrior:

    def __init__(self, strength, agility, stamina, intellect):
        totalStats = strength + agility + stamina+ intellect
        self.strength = strength
        self.agility = agility
        self.stamina = stamina
        self.intellect = intellect
        self.wounds = 0

        self.hitpoints = (self.strength*5 + self.intellect)*self.stamina
        self.evasion = (self.agility + self.intellect)/totalStats
        
    
    def getRemainingHitpoints(self):
        hitpoints = (self.strength*5 + self.intellect)*self.stamina - self.wounds
        return hitpoints



Mike = Warrior(20, 20, 20, 20)

print(Mike.getRemainingHitpoints())

Mike.wounds = 1000

print(Mike.getRemainingHitpoints())