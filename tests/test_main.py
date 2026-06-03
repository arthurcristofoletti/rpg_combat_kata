from src.main import start_player, damage_player, heal_player


def test_main_pipeline_execution():
    """Validates that the main application entry point runs successfully."""
    player = start_player("Test")
    damage_player(player, "200")
    heal_player(player, "200")
    assert player.health == 1000


