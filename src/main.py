from src.app import character as personnage

def start_player() -> personnage:
    player_name=input("Name of the character: ")
    return personnage(player_name)

def damage_player(player):
    ammount=input("Ammount of damage: ")
    player.take_damage(int(ammount))

def heal_player(player):
    ammount=input("Ammount of heal: ")
    player.take_heal(int(ammount))

if __name__ == "__main__":
    print("Starting game....")
    p1=start_player()
    damage_player(p1)
    heal_player(p1)

    
