from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from typing import Any


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simul: int = 0
        self.cards: dict[str, list[Card]] = {}
        self.cards_created: int = 0
        self.total_damage: int = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict[str, Any]:
        if not self.factory or not self.strategy:
            raise ValueError("Engine must be configured first:" +
                             "Factory and Strategy not configure!")
        deck_data = self.factory.create_themed_deck(3)
        hand = deck_data['deck']
        self.cards['player 1'] = hand
        self.cards_created += len(hand)
        battlefield = [10, ['Enemy Player', 'Enemy Goblin']]
        turn_result = self.strategy.execute_turn(hand, battlefield)
        damage = turn_result['actions'].get('damage_dealt', 0)
        self.total_damage += damage
        self.turns_simul += 1
        return turn_result

    def get_engine_status(self) -> dict[str, Any]:
        if not self.strategy:
            strategy_name = "None"
        else:
            strategy_name = self.strategy.get_strategy_name()
        return {
            'turns_simulated': self.turns_simul,
            'strategy_used': strategy_name,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
