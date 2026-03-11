from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    print(f"Factory: {engine.factory.__class__.__name__}")
    if engine.strategy:
        print(f"Strategy: {engine.strategy.get_strategy_name()}")
    turn = engine.simulate_turn()
    cards_available = engine.cards['player 1']
    print(f"Available types: {factory.get_supported_types()}")
    print("\nSimulating aggressive turn...")
    print(f"Hand: {cards_available} ")
    print("\nTurn execution:")
    print(f"Strategy: {turn['strategy']}")
    print(f"Actions: {turn['actions']}")
    print("\nGame Report:")
    print(engine.get_engine_status())
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
