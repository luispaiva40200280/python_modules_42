from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from tools.card_generator import CardGenerator


GAME_STATE = {
    'available_mana': 100,
    'name': 'MODULE THE PYTHON 07',
    'playable': True
}


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")
    generator = CardGenerator()
    raw_data: list[dict] = generator.generate_random_deck(20)
    my_cards: list[Card] = []
    for data in raw_data:
        if 'attack' in data:
            my_cards.append(CreatureCard(**data))
        elif "durability" in data:
            my_cards.append(ArtifactCard(**data))
        elif "effect_type" in data:
            my_cards.append(SpellCard(**data))
    print("Building deck with different card types...")
    my_deck = Deck(my_cards)
    print(my_deck.get_deck_stats())
    print()
    print("Drawing and playing cards:")
    for _ in range(3):
        try:
            drew_card = my_deck.draw_card()
            print(f"Drew: {drew_card.name} ({drew_card.__class__.__name__})")
            print(f"Play result: {drew_card.play(GAME_STATE)}")
            print()
        except Exception:
            print("Deck is empty")
    print("Polymorphism in action: Same interface," +
          " different card behaviors!")


if __name__ == "__main__":
    main()
