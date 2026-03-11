from typing import Any


class Player:
    def __init__(self, name: str, score: int) -> None:
        self.name: str = name
        self.score: int = score
        self.active: bool = False
        self.achievements: list = []
        self.regions: dict[str, bool] = {
            "basic": True,
        }

    def add_achievements(self, achievement: Any) -> None:
        try:
            if type(achievement) is not str:
                lst_achivments = iter(achievement)
                while True:
                    try:
                        achievement = next(lst_achivments)
                        self.achievements.append(achievement)
                    except StopIteration:
                        break
        except TypeError:
            self.achievements.append(achievement)

    def add_regions(self, region_name: str, status: bool = True) -> None:
        # Dictionary syntax: self.dict[key] = value
        self.regions[region_name] = status

    def __repr__(self) -> str:
        return f"Player {self.name}: {self.score}"


# initialize list of players
def init_data() -> set:
    player_set: set = set()
    names: list[str] = [
        "Alice", "Bob", "Charlie", "Diana", "Eve",
        "Frank", "Grace", "Hank", "Ivy", "Jack"]

    for i in range(3):
        name: str = names[i]
        score: float = ((i + 1) * 57) % 100
        new_player: Player = Player(name, score)
        if i % 2 == 0:
            new_player.active = True
            new_player.add_achievements(["boss_slayer"])
        else:
            new_player.add_achievements(["first_kill", "level_10"])
            new_player.active = False
        player_set.add(new_player)
    max_level: int = max(p.score for p in player_set)
    for p in player_set:
        if p.score == max_level:
            p.add_achievements("Best player")
            p.add_regions("last", False)
        p.add_regions("north", True)
        p.add_regions("south", False)
    return player_set


def main() -> None:
    data_base: set[Player] = init_data()
    print("=== Game Analytics Dashboard ===\n")
    print(f"Database created with {len(data_base)} players:")
    print(f"Database created with {data_base} players:\n")

    print("\n=== List Comprehension Examples ===")
    high_scores_name: list[str] = [p.name for p in data_base if p.score > 50]
    high_scores_double: list[int] = [
        p.score * 2 for p in data_base if p.active
        ]
    active_users: list[str] = [p.name for p in data_base if p.active]
    print(f"High scorers (>50): {high_scores_name}")
    print(f"Scores doubled: {high_scores_double}")
    print(f"Active users: {active_users}")
    print()
    print("=== Dict Comprehension Examples ===")
    players_scores: dict[str, int] = {p.name: p.score for p in data_base}
    score_categories: dict[str, int] = {
        "high": len([p for p in data_base if p.score > 70]),
        "medium": len([p for p in data_base if 40 <= p.score <= 70]),
        "low": len([p for p in data_base if p.score < 40])
    }
    achievement_count: dict[str, int] = {
        p.name: len(p.achievements) for p in data_base
        }
    print()
    print(f"Player scores: {players_scores}")
    print(f"Score categories: {score_categories}")
    print(f"achievement count: {achievement_count}")
    print()
    print("=== Set Comprehension Examples ===")
    unique_names: set[str] = {p.name for p in data_base}
    unique_achievements: set[str] = {
        ach for p in data_base for ach in p.achievements
        }
    active_regions: set[str] = {
        region for p in data_base
        for region, status in p.regions.items()
        if status is True}
    print(f"Unique names: {unique_names}")
    print(f"Unique achievement: {unique_achievements}")
    print(f"Active regions: {active_regions}")
    print()
    print("=== Combined Analysis ===")
    print(f"Total players: {len(data_base)}")
    print(f"Total unique_achievements: {len(unique_achievements)}")
    print("Average score:" +
          f"{sum(p.score for p in data_base) / len(data_base):.1f}")
    max_score: int = max(p.score for p in data_base)
    top_perf: list[Player] = [
        player for player in data_base if player.score == max_score
        ]
    print(f"Top performer: {top_perf[0].name} " +
          f"({top_perf[0].score} points, " +
          f"{len(top_perf[0].achievements)} achievements)")


if __name__ == "__main__":
    main()
