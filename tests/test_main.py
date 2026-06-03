
from src.main import start_player, damage_player, heal_player


def test_main_pipeline_execution():
    """Validates that the main application entry point runs successfully."""
    # Simulate the main application flow
    player_name = "TestPlayer"
    p1 = start_player(player_name)
    assert p1.name == player_name
    assert p1.health == 1000
    assert p1.level == 1
    assert p1.alive
    player_name = "TestPlayer2"
    p2 = start_player(player_name)
    assert p2.name == player_name
    assert p2.health == 1000
    assert p2.level == 1
    assert p2.alive
    # Simulate damage and healing
    damage_player(p1, p2, "200")
    assert p2.health == 800

    heal_player(p2, "100")
    assert p2.health == 900
