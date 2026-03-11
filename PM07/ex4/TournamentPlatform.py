from ex4.TournamentCard import TournamentCard
from typing import Any


class TournamentPlatform():
    def __init__(self) -> None:
        self.cards_in_match: dict[str, TournamentCard] = {}
        self.matches: int = 0

    def register_card(self, card: TournamentCard) -> str:
        if card.name not in self.cards_in_match:
            self.cards_in_match[card.name] = card
            return f"{card.name} registerd in the Tournment"
        return f"{card.name} is already in the Tournment"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if (card1_id not in self.cards_in_match
                or card2_id not in self.cards_in_match):
            raise ValueError("Both cards must be registered to fight!")

        card1 = self.cards_in_match[card1_id]
        card2 = self.cards_in_match[card2_id]

        card1.attack(card2)
        if card2.health > 0:
            card2.attack(card1)
        if card1.health >= card2.health:
            winner = card1
            losser = card2
        else:
            winner = card2
            losser = card1
        winner.update_wins(1)
        losser.update_losses(1)
        self.matches += 1
        return {
            'winner': winner.name,
            'loser': losser.name,
            'winner_rating': winner.rating,
            'loser_rating': losser.rating
        }

    def get_leaderboard(self) -> list:
        def sort_by_rating(card: TournamentCard) -> int:
            return card.rating
        sorted_cards = sorted(
            self.cards_in_match.values(),  # <- the list i want to sort,
            key=sort_by_rating,  # <- the paramter that i want to sort
            reverse=True  # <- change the defoult behaveor of the sorting
        )
        leaderboard = []
        for card in sorted_cards:
            leaderboard.append(f"{card.name} - Rating: {card.rating} " +
                               f"({card.get_rank_info()['Record']})")
        return leaderboard

    def generate_tournament_report(self) -> dict[str, Any]:
        nbr_cards = len(self.cards_in_match)
        total = sum(
            card.rating for card in self.cards_in_match.values()
        )
        avg = total / nbr_cards if nbr_cards > 0 else 0.0
        return {
            'total_cards': nbr_cards,
            'matches_played': self.matches,
            'avg_rating': round(avg, 2),
            'platform_status': 'active'
            }
