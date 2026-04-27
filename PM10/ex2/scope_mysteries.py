from typing import Callable, Any


def mage_counter() -> Callable:
    """
    This function demonstrates Closures and lexical scoping.
    It initializes a local `count` variable and defines an inner function
    that increments and returns this count. Because the inner function is
    returned, it creates a "closure" a protective memory bubble around
    the `count` variabl
    """
    count = 0

    def inner_counter() -> int:
        """
        The inner function uses the `nonlocal` keyword to explicitly tell
        Python to modify the `count` variable from the outer scope
        """
        nonlocal count
        count += 1
        return count
    return inner_counter


def spell_accumulator(initial_power: int) -> Callable:
    def accumulator(amount: int) -> int:
        nonlocal initial_power
        initial_power += amount
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value
        print(f"Stored: {key} -> {value}")

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")
    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print("=== Using nonlocal variabeles to simulate static variables===")
    counter = mage_counter()
    print(f"Inicial counter: {counter()}")
    for _ in range(1, 10):
        counter()
    print(f"Counter was call: {counter()} times\n")
    power = 10
    magic_power = spell_accumulator(power)
    for i in range(1, 5):
        power = magic_power(i)
        print(f"Power increise: {i} -> result: {power}")
    print(f"Final power: {power}\n")
    print("Testing enchantment factory...")
    flaming_factory = enchantment_factory("Flaming")
    flaming_sword = flaming_factory("sword")
    print(f"Enchant item created: {flaming_sword}")
    ice_factory = enchantment_factory("Ice")
    ice_sheild = ice_factory("Shield")
    print(f"Enchant item created: {ice_sheild}")
    print()
    print("=== Testing Memory Vault ===")
    vault = memory_vault()
    print("Storing ice and fire spell in the vault...")
    vault['store']('ice_spell', "iceball")
    vault['store']('fire_spell', "fireball")
    print("Recalling the spells...")
    print(f"Recalling Ice spell: {vault['recall']('ice_spell')}")
    print(f"Recalling Fire spell: {vault['recall']('fire_spell')}")
    print("See something there is not in the vault: " +
          f"{vault['recall']('empty')}")


if __name__ == "__main__":
    main()
