class Achievement:
    """A simple objct to create my achivements"""
    def __init__(self, name: str, rarity: str) -> None:
        self.name: str = name
        self.rarity: str = rarity


class Player:
    """A player that holds achivements"""
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.achievements: list[Achievement] = []

    def add_achievement(self, achivement: Achievement) -> None:
        self.achievements.append(achivement)

    def get_achievements(self) -> set[str] | set:
        achs: set[str] = {ach.name for ach in self.achievements}
        return achs


def init_achievement_data() -> list[Player]:
    """Creates a diverse set of players and achievements for set analysis."""
    ach_first_kill: Achievement = Achievement("First Kill", "Common")
    ach_collector: Achievement = Achievement("Collector", "Common")
    ach_boss_slayer: Achievement = Achievement("Boss Slayer", "Rare")
    ach_speed_run: Achievement = Achievement("Speed Demon", "Unique")
    ach_hidden_gem: Achievement = Achievement("Hidden Gem", "Unique")

    alice: Player = Player("Alice")
    bob: Player = Player("Bob")
    charlie: Player = Player("Charlie")

    for p in [alice, bob, charlie]:
        p.add_achievement(ach_first_kill)
        p.add_achievement(ach_collector)

    alice.add_achievement(ach_boss_slayer)
    bob.add_achievement(ach_boss_slayer)

    alice.add_achievement(ach_speed_run)
    charlie.add_achievement(ach_hidden_gem)

    return [alice, bob, charlie]


def acievement_traker() -> None:
    players: list[Player] = init_achievement_data()
    print("=== Achievement Tracker System ===\n")
    for p in players:
        print(f"Player {p.name} achivements : {p.get_achievements()}")
    print()

    # a set of all achivements
    players_ach: list[set[str]] = [p.get_achievements() for p in players]
    if not players_ach:
        print("No players found to analyze.")
        return

    # Union: Every achievement discovered in the game
    all_discovered = set().union(*players_ach)
    print(f"All unique achievements: {all_discovered}")
    print(f"Total unique achievements: : {len(all_discovered)}\n")

    # This finds commonality (e.g., 'First Kill' and 'Collector')
    common_to_all: set[str] = set.intersection(*players_ach)
    print(f"Common to all players: {common_to_all}")

    # player has the achievement
    rare_ach: set[str] = {
        ach for ach in all_discovered
        if sum(1 for s in players_ach if ach in s) == 1
        }
    print(f"Rare achievements (1 player): {rare_ach}")

    # compare 2 players
    alice_unique: set[str] = players_ach[0].difference(players_ach[1])
    print(f"Alice has these that Bob doesn't: {alice_unique}")


if __name__ == "__main__":
    acievement_traker()
