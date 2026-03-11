from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex3.GameStrategy import GameStrategy
from typing import Any


class AggressiveStrategy(GameStrategy):
    def prioritize_targets(self, available_targets: list[Card]) -> list:
        def sorted_for_mosters(target: Card) -> bool:
            return isinstance(target, CreatureCard)
        return (available_targets.sort(key=sorted_for_mosters, reverse=True)
                or available_targets)

    def execute_turn(self, hand: list[Card],
                     battlefield: list[Any]) -> dict[str, Any]:
        current_mana = 5
        cards_played = []
        damage_dealt = 0
        mana_used = 0
        targets = ["Enemy Player"]

        sorted_hand = sorted(hand, key=lambda card: card.cost)

        for card in sorted_hand:
            if card.cost <= current_mana:
                current_mana -= card.cost
                mana_used += card.cost
                cards_played.append(card.name)
                if isinstance(card, CreatureCard) and hasattr(card, 'attack'):
                    damage_dealt += card.attack
                elif isinstance(card, SpellCard):
                    if (hasattr(card, 'effect_type') and
                            card.effect_type == "damage"):
                        damage_dealt += card.effect_amount()

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": targets,
                "damage_dealt": damage_dealt
            }
        }

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'
