from ex0.Card import Card
from ex2.Combatable import Combatable, Types
from ex4.Rankable import Rankable
from typing import Any


class TournamentCard(Card, Combatable, Rankable):
    BASE_RATING: int = 1200

    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, health: int, card_type: str,
                 base_rating: int = BASE_RATING) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.type = card_type
        self.wins = 0
        self.losses = 0
        self.rating = base_rating

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, value: str) -> None:
        if value not in Combatable.VALID_TYPES:
            raise ValueError(f"Invalid type: '{value}'. " +
                             f"Must be one of {Combatable.VALID_TYPES}")
        self.__type = value

    def play(self, game_state: dict) -> dict[str, Any]:
        mana = game_state.get("available_mana", 0)
        if not self.is_playable(mana):
            return {'Playable': False}
        game_state["available_mana"] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'Playable': True
            }

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
        match self.__type:
            case Types.Warrior.value | Types.Magician.value:
                raw_defence = incoming_damage * 0.45
            case Types.Tank.value:
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
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            'card': self.name,
            'power': self.attack_power,
            'health': self.health
        }

    def calculate_rating(self) -> int:
        self.rating = round(self.BASE_RATING + (self.wins * 16)
                            - (self.losses * 16))
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> dict[str, Any]:
        return {
            'Rating': self.rating,
            'Record': f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict[str, Any]:
        return {
            'card': self.name,
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses,
            'status': 'Active' if self.health > 0 else 'Defeated'
        }

    def get_bases_cls(self) -> str:
        interfaces_bass = [base.__name__ for base in self.__class__.__bases__]
        return f"Interfaces: {interfaces_bass}"
