class Character:
    def __init__(self, health = 10, defense = 10):
        self.health = health
        self.defense = defense
    
    def attack(self, other):
        damage = 20-other.defense
        other.health -= damage