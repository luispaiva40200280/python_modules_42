from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory
from typing import Union, Any
from random import choice


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._creatures = {
            "dragon": {"name": "Fire Dragon", "cost": 5, "rarity": "Legendary",
                       "attack": 7, "health": 5},
            "goblin": {"name": "Goblin Warrior", "cost": 2, "rarity": "Common",
                       "attack": 2, "health": 2}
        }
        self._spells = {
            "fireball": {"name": "Fireball", "cost": 3, "rarity": "Rare",
                         "effect_type": "damage"},
            "lightning": {"name": "Lightning Bolt", "cost": 3,
                          "rarity": "Common", "effect_type": "damage"}
        }
        self._artifacts = {
            "mana_ring": {"name": "Mana Ring", "cost": 2, "rarity": "Uncommon",
                          "durability": 3, "effect": "mana_boost: +5 of mana"},
            "pote": {"name": "Pote", "cost": 2, "rarity": "Uncommon",
                     "durability": 3, "effect": "mana_boost: +5 of mana"}
        }

    def get_card(self, registry: dict, identifier:
                 Union[str, int, None] = None) -> dict[str, Any]:
        if isinstance(identifier, str):
            template = registry.get(identifier.lower())
            if template:
                return template
        elif isinstance(identifier, int):
            for template in registry.values():
                if template["cost"] == identifier:
                    return template
        return choice(list(registry.values()))

    def create_creature(self, name_or_power:
                        Union[str, int, None] = None) -> Card:
        templete = self.get_card(self._creatures, name_or_power)
        return CreatureCard(**templete)

    def create_spell(self, name_or_power:
                     Union[str, int, None] = None) -> Card:
        templete = self.get_card(self._spells, name_or_power)
        return SpellCard(**templete)

    def create_artifact(self, name_or_power:
                        Union[str, int, None] = None) -> Card:
        templete = self.get_card(self._artifacts, name_or_power)
        return ArtifactCard(**templete)

    def create_themed_deck(self, size: int = 1) -> dict[str, Any]:
        deck: list[Card] = []
        factory_methods: list[Any] = [
            self.create_creature,
            self.create_spell,
            self.create_artifact
        ]
        for _ in range(size):
            random_creator = choice(factory_methods)
            card = random_creator()
            deck.append(card)
        return {
            'theme': 'Fantasy',
            'size': size,
            'deck': deck
        }

    def get_supported_types(self) -> dict[str, Any]:
        return {
            'creatures': list(self._creatures.keys()),
            'spells': list(self._spells.keys()),
            'artifacts': list(self._artifacts.keys())
        }
