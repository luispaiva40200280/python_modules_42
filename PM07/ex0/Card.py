from typing import Any
from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    VALID_RARITIES: list[str] = [r.value for r in Rarity]
    __rarity: str

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @property
    def rarity(self) -> str:
        return self.__rarity

    # 3. The Setter (The Security Checkpoint)
    @rarity.setter
    def rarity(self, value: str) -> None:
        # We validate 'value' here instead of in __init__
        if value not in Card.VALID_RARITIES:
            raise ValueError(f"Invalid rarity: '{value}'. " +
                             f"Must be one of {Card.VALID_RARITIES}")
        self.__rarity = value

    @abstractmethod
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

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost

    def __repr__(self) -> str:
        return (f"{self.name} ({self.cost})")
