class character:
    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.level = 1
        self.alive = True

    def take_damage(self, ammount: int):
        if self.health-ammount <= 0:
            self.alive=False
            self.health=0
        else:
            self.health-=ammount

    def take_heal(self, ammount: int):
        if self.alive and ammount >= 0:
           if self.health+ammount > 1000:
               self.health=1000
           else:
               self.health+=ammount
        else:
            raise ValueError("Heal impossible")
