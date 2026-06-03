from src.app import character as personnage
from src.main import start_player, damage_player, heal_player


def test_main_pipeline_execution():
    """Validates that the main application entry point runs successfully."""
    player = start_player()
    damage_player(player)
    heal_player(player)
    assert player.health == 1000


