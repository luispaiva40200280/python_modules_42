from ex0.Card import Card


class CreatureCard(Card):
    __attack: int
    __health: int

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    @property
    def attack(self) -> int:
        return self.__attack

    @attack.setter
    def attack(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Attack must be a positive integer.")
        self.__attack = value

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Health must be a positive integer.")
        self.__health = value

    def play(self, game_state: dict) -> dict:
        result = super().play(game_state)
        result['effect'] = 'Creature summoned to battlefield'
        return result

    def attack_target(self, target: "CreatureCard") -> dict:
        combat = True if target.health - self.attack == 0 else False
        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack,
            'combat_resolved': combat
            }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = 'Creature'
        info['attack'] = self.attack
        info['health'] = self.health
        return info
