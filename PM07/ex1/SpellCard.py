from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from enum import Enum


class SpellType(Enum):
    HEALING = 'Heal'
    DAMAGE = 'Damage'
    BUFF = 'Buff'


class SpellCard(Card):
    VALID_SPELLS: list[str] = [s.value for s in SpellType]

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    @property
    def effect_type(self) -> str:
        return self.__effect_type

    @effect_type.setter
    def effect_type(self, value: str) -> None:
        capitalized_value = value.capitalize()
        if capitalized_value not in SpellCard.VALID_SPELLS:
            raise ValueError("Invalid spel type '{}'. Must be one of {}"
                             .format(value, SpellCard.VALID_SPELLS))
        self.__effect_type = capitalized_value

    def effect_amount(self) -> int:
        count: int = 0
        match self.rarity:
            case 'Common':
                count = 1
            case 'Uncommon':
                count = 3
            case 'Rare':
                count = 5
            case 'Legendary':
                count = 10
            case _:
                return 0
        return count

    def resolve_effect(self, targets: list['Card']) -> dict:
        if not targets:
            return {'Targets': 'None'}
        count = self.effect_amount()
        match self.effect_type:
            case 'Healing':
                for card in targets:
                    if isinstance(card, CreatureCard):
                        card.health += count
                    elif isinstance(card, ArtifactCard):
                        card.durability += count
            case 'Damage':
                for card in targets:
                    if isinstance(card, CreatureCard):
                        card.health -= count
                    elif isinstance(card, ArtifactCard):
                        card.durability -= count
            case 'Buff':
                for card in targets:
                    if isinstance(card, CreatureCard):
                        card.attack += count
                    elif isinstance(card, ArtifactCard):
                        card.durability += count
        targets_names = [card.name for card in targets]
        return {
            'name': self.name,
            'type': self.effect_type,
            'targets': targets_names
        }

    def play(self, game_state: dict) -> dict:
        result = super().play(game_state)
        result['effect'] = self.effect_type
        return result
