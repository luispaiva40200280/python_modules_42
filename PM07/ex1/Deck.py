from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from random import shuffle as shuff


class Deck():
    def __init__(self, card_deck: list[Card]) -> None:
        self.card_deck: list[Card] = card_deck

    def add_card(self, card: Card) -> None:
        self.card_deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.card_deck:
            if card.name == card_name:
                self.card_deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        if not self.card_deck:
            return
        shuff(self.card_deck)

    def draw_card(self) -> Card:
        return self.card_deck.pop()

    def get_deck_stats(self) -> dict:
        total = len(self.card_deck) if self.card_deck else 0
        if total == 0:
            avg = 0
        else:
            avg = round(sum([card.cost for card in self.card_deck]) / total, 1)
        return {
            'total_cards': total,
            'creatures': len([
                card for card in self.card_deck
                if isinstance(card, CreatureCard)]),
            'spells': len([
                card for card in self.card_deck
                if isinstance(card, SpellCard)]),
            'artifacts': len([
                card for card in self.card_deck
                if isinstance(card, ArtifactCard)]),
            'avg_cost': avg
            }
