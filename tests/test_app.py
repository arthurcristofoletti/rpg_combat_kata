from src.app  import character

def test_character_creation():
    char = character("Test")
    assert char.name == "Test"
    assert char.health == 1000
    assert char.level == 1
    assert char.alive
def test_character_take_damage():
    char = character("Test")
    char.take_damage(200)
    assert char.health == 800
    char.take_damage(800)
    assert char.health == 0
    assert not char.alive
def test_character_heal():
    char = character("Test")
    char.take_damage(500)
    char.take_heal(200)
    assert char.health == 700
    char.take_heal(500)
    assert char.health == 1000
    assert char.alive
