from ex2.Combatable import Types
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")
    tournament = TournamentPlatform()
    card1 = TournamentCard("Fire Dragon", 20, "Legendary", 70, 50,
                           Types.Warrior.value)
    card2 = TournamentCard("Goblin Warrior", 50, "Legendary", 80, 50,
                           Types.Warrior.value)
    tournament.register_card(card1)
    tournament.register_card(card2)

    print(f"{card1.name} (ID: dragon_001)")
    print(f"- {card1.get_bases_cls()}")
    print(f"- Rating: {card1.get_rank_info()['Rating']}")
    print(f"- Record: {card1.get_rank_info()['Record']}")
    print(f"{card2.name} (ID: wizard_001))")
    print()
    print(f"- {card2.get_bases_cls()}")
    print(f"- Rating: {card2.get_rank_info()['Rating']}")
    print(f"- Record: {card2.get_rank_info()['Record']}")
    print("\nCreating tournament match...")
    print("Match result: {}"
          .format(tournament.create_match(card1.name, card2.name)))

    print("Tournament Leaderboard:")
    for nbr, leaders in enumerate(tournament.get_leaderboard(), start=1):
        print(f"{nbr}. {leaders}")
    print("Platform Report:")
    print(tournament.generate_tournament_report())
    print("\n=== Tournament Platform Successfully Deployed! ===\n" +
          "All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
