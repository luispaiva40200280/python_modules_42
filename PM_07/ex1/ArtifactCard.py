from ex0.Card import Card


class ArtifactCard(Card):
    __durability: int
    __effect: str

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    @property
    def durability(self) -> int:
        return self.__durability

    @durability.setter
    def durability(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Durability must be a positive integer.")
        self.__durability = value

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, value: str) -> None:
        if not isinstance(value, str) or ":" not in value:
            raise ValueError(f"{value} is not a valid effect.")
        self.__effect = value

    def activate_ability(self) -> dict:
        self.durability -= 1
        return {
            'name': self.name,
            'duration': self.__effect.split(":")[0].strip(),
            'effect': self.__effect.split(":")[1].strip(),
            'durability left': self.durability
        }

    def play(self, game_state: dict) -> dict:
        result = super().play(game_state)
        result['effect'] = self.__effect
        return result
