from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Any


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, health: int, mana_pool: int,
                 type: str) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.mana_pool = mana_pool
        self.type = type

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, value: str) -> None:
        if value not in Combatable.VALID_TYPES:
            raise ValueError(f"Invalid type: '{value}'. " +
                             f"Must be one of {Combatable.VALID_TYPES}")
        self.__type = value

    def attack(self, target: Card) -> dict[str, Any]:
        if isinstance(target, Combatable):
            defence = target.defend(self.attack_power)['damage_blocked']
            damage = int(max(0, self.attack_power - defence))
        else:
            damage = self.attack_power
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': damage,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        # FIX 2: Fixed spelling and removed parentheses
        match self.__type:
            case 'Warrior' | 'Magician':
                raw_defence = incoming_damage * 0.45
            case 'Tank':
                raw_defence = incoming_damage * 0.75
            case _:
                raw_defence = 3
        defence = int(raw_defence)
        actual_damage = max(0, incoming_damage - defence)
        self.health -= actual_damage
        return {
            'defender': self.name,
            'damage_taken': actual_damage,
            'damage_blocked': defence,
            # FIX 3: Fixed the zombie bug!
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            'card': self.name,
            'type': self.__type,
            'mana': self.mana_pool,
            'attack_power': self.attack_power
        }

    def cast_spell(self, spell_name: str,
                   targets: list[Card]) -> dict[str, Any]:
        return {
            'caster': self.name,
            'spell': spell_name,  # FIX 5: Fixed typo
            'attack_power': self.attack_power,
            'targets': [card.name for card in targets],
            'mana_used': 4,
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        self.mana_pool += amount
        return {
            'channeled': amount,
            'total_mana': self.mana_pool
        }

    def get_magic_stats(self) -> dict[str, Any]:
        info = super().get_card_info()
        info['attack_power'] = self.attack_power
        info['health'] = self.health
        info['mana_pool'] = self.mana_pool
        return info

    def play(self, game_state: dict) -> dict:
        result = super().play(game_state)
        result['mana'] = self.mana_pool
        result['health'] = self.health
        result['effect'] = 'Creature summoned to battlefield'
        return result
