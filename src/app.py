class character:
    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.level = 1
        self.alive = True

    def get_level(self):
        return self.level

    def display_status(self):
        print(f"Name: {self.name}, Health: {self.health}, Level: {self.level}, Alive: {self.alive}")

    def take_damage(self, ammount: int):
        if self.health-ammount <= 0:
            self.alive=False
            self.health=0
        else:
            self.health-=ammount

    def damage_player(self, player, ammount: int):
        if player != self and player.alive:
            if player.get_level() >= self.get_level()+5:
                ammount=int(ammount*0.5)
            if player.get_level() <= self.get_level()-5:
                ammount=int(ammount*1.5)
            player.take_damage(ammount)


    def take_heal(self, ammount: int):
        if self.alive and ammount >= 0:
           if self.health+ammount > 1000:
               self.health=1000
           else:
               self.health+=ammount
        else:
            raise ValueError("Heal impossible")

    def heal_player(self, player, ammount):
        if player == self:
            self.take_heal(int(ammount))
