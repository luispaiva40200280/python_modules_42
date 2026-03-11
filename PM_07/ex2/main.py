from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    hero = EliteCard("Arcane Warrior", 5, "Legendary", 5, 10, 4, "Magician")
    enemy = EliteCard("Armored Troll", 4, "Rare", 3, 15, 0, "Tank")

    print("EliteCard capabilities:")
    card_methods: list[str] = [
        method for method in dir(Card) if callable(getattr(Card, method))
        and not method.startswith('_')
                  ]
    print(f"- Card: {card_methods}")
    combatable_methods: list[str] = [
        method for method in dir(Combatable)
        if callable(getattr(Combatable, method)) and not method.startswith('_')
        ]
    print(f"- Combatable: {combatable_methods}")
    magic_methods: list[str] = [
        method for method in dir(Magical) if callable(getattr(Magical, method))
        and not method.startswith('_')
    ]
    print(f"- Magical: {magic_methods}")
    print()
    print(f"Playing {hero.name} (Elite Card):\n")
    print("Combat phase:")
    print(f"Attack result: {hero.attack(enemy)}")
    print(f"Deffence result: {hero.defend(5)}")
    print()
    print("Magic phase:\n")
    print(f"Spell cast: {hero.cast_spell('Fireball', [enemy])}")
    print(f"Mana channel: {hero.channel_mana(3)}")
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
