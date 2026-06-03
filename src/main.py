from src.app import character as personnage

def start_player() -> personnage:
    player_name=input("Name of the character: ")
    return personnage(player_name)

def damage_player(player, ammount):
    player.take_damage(int(ammount))

def heal_player(player,ammount):
    player.take_heal(int(ammount))

if __name__ == "__main__":
    print("Starting game....")
    p1=start_player()
    ammount=input("Ammount of damage: ")
    damage_player(p1, ammount)
    ammount=input("Ammount of heal: ")
    heal_player(p1, ammount)

    
