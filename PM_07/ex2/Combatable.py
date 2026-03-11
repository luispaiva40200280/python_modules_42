from abc import ABC, abstractmethod
from enum import Enum


class Types(Enum):
    Warrior = 'Warrior'
    Magician = 'Magician'
    Tank = 'Tank'


class Combatable(ABC):
    VALID_TYPES: list[str] = [t.value for t in Types]

    @abstractmethod
    def attack(self, target) -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
