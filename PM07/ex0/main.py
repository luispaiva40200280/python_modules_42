from ex0.CreatureCard import CreatureCard
from tools.card_generator import CardGenerator
import random

GAME_STATE = {
    'available_mana': 10,
    'name': 'MODULE THE PYTHON 07',
    'playable': True
}


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:")

    all_cards: list[CreatureCard] = []
    for creature in CardGenerator().get_all_creatures():
        name, cost, rarity, attack, health = creature.values()
        card = CreatureCard(name, cost, rarity, attack, health)
        all_cards.append(card)

    attack = random.choice(all_cards)
    target = random.choice(all_cards)
    mana = GAME_STATE["available_mana"]
    print("CreatureCard Info:")
    print(attack.get_card_info())
    print()
    print("Playing {} with {} mana available:"
          .format(attack.name, mana))
    print("Playable: {}"
          .format(attack.is_playable(mana)))
    print("Play result: {}"
          .format(attack.play(GAME_STATE)))

    print()
    print("{} attacks {}:"
          .format(attack.name, target.name))
    print("Attack result: {}"
          .format(attack.attack_target(target)))
    print()
    print("Testing insufficient mana (3 available):")
    print("Playable: {}"
          .format(all_cards[0].is_playable(3)))
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
