from src.app import character

def start_player(player_name) -> character:
    return character(player_name)

def damage_player(self, player: character, ammount: str):
    player.take_damage(int(ammount))

def heal_player(self, ammount: str):
    self.take_heal(int(ammount))

if __name__ == "__main__":
    print("Starting game....")
    player_name=input("Name of the character: ")
    p1=start_player(player_name)
    p1.display_status()
    player_name=input("Name of the character: ")
    p2=start_player(player_name)
    p2.display_status()
    print("Player 1 attacks player 2")
    ammount=input("Ammount of damage of player 1 in player 2: ")
    damage_player(p1, p2, ammount)
    print("Player 1 successfully attacked player 2")
    p2.display_status()
    #ammount=input("Ammount of heal: ")
    #heal_player(p1, ammount)
    #print(f"Success: {p1.health}")
