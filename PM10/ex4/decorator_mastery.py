from typing import Callable, Any
from functools import wraps
from time import time, sleep


def spell_timer(func: Callable) -> Callable:
    """
    A simple decorator that acts as a stopwatch for any function.
    WHAT IT DOES:
    This decorator lets you measure exactly how long a function takes to run
    without having to rewrite the code inside the function itself.
    It physically  "wraps" your function in a start-clock and
    stop-clock sequence.
    """
    @wraps(func)
    def timer(*args: Any, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Spell completed in {(end - start):.4f} seconds")
        return result
    return timer


def power_validator(min_power: int) -> Callable:
    """
    Because this decorator takes its own argument (min_power),
    it requires a three-layer architecture to work properly:
    -> Takes the safety rule (min_power) and remembers it.
    -> (wrapper): Takes the specific function (func) you want to protect
    -> The active guard. When the function is finally
       called, it checks the first argument (*args[0]). If it meets
       the requirement, it allows the function to run. If not,
       it blocks execution.
    """
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def validator(*args: Any, **kwargs: Any) -> Any:
            power = next((arg for arg in args if isinstance(arg, int)), None)
            if power is None or not args or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return validator
    return wrapper


def retry_spell(max_attempts: int) -> Callable:

    def wrapper(func: Callable) -> Callable:

        @wraps(func)
        def attempts(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying..." +
                          f"attempt ({attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return attempts
    return wrapper


class MageGuild:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (len(name) >= 3 and name.replace(" ", "").isalpha())

    @spell_timer
    @power_validator(10)
    @retry_spell(3)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """A basic spell to test our stacked decorators."""
        # 1. 50% chance the spell completely crashes!
        if self.power < power:
            raise ValueError("Insuficient mana!")
        sleep(1)
        return f"The {spell_name} spell was launched!"


def main() -> None:
    print("=== Testing Stacked Decorators ===")
    mage = MageGuild("Dumbledore", 10)
    print(f"{mage.name} is valid => " +
          f"{mage.validate_mage_name('Dumbledore')}")

    # Test 1: Not enough power (Fails the validator)
    print("\n--- Casting with 3 Power ---")
    weak_cast = mage.cast_spell("Fireball", 3)
    print(f"Result: {weak_cast}")

    # Test 2: Enough power (Passes the validator)
    print("\n--- Casting with 10 Power ---")
    strong_cast = mage.cast_spell("Fireball", 10)
    print(f"Result: {strong_cast}")

    print("\n--- Casting multipel times ---")
    cast = mage.cast_spell("Fireball", 50)
    print(cast)


if __name__ == "__main__":
    main()
