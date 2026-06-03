from src.app import character

def start_player(player_name) -> character:
    return character(player_name)

def damage_player(player: character, ammount: str):
    player.take_damage(int(ammount))

def heal_player(player: character, ammount: str):
    player.take_heal(int(ammount))

if __name__ == "__main__":
    print("Starting game....")
    player_name=input("Name of the character: ")
    p1=start_player(player_name)
    ammount=input("Ammount of damage: ")
    damage_player(p1, ammount)
    ammount=input("Ammount of heal: ")
    heal_player(p1, ammount)
    print(f"Success: {p1.health}")
