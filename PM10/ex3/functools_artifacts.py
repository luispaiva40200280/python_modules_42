from typing import Callable, TypedDict, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator
from time import time


def spell_reducer(spells: list[int], operation: str) -> int | str:
    """
    Reduce: returns a list or numb or string, depending
    on the op that we pass to it with a list of data
    """
    try:
        match operation:
            case 'add':
                return reduce(operator.add, spells)
            case 'multiply':
                return reduce(operator.mul, spells)
            case 'sub':
                return reduce(operator.sub, spells)
            case 'max':
                return reduce(max, spells)
            case 'min':
                return reduce(min, spells)
            case _:
                raise ValueError("Operation not defined: needs to" +
                                 " be one of ['add', multiply, sub, max, min]")
    except ValueError as e:
        return str(e)


class ITEM(TypedDict):
    name: str
    power: int
    durability: float
    enchant: str


def enchantment(increase: int, type: str, item: ITEM) -> str:
    match type:
        case 'fire':
            item['power'] += increase
            item['enchant'] = f"fire {item['name']}"
        case 'ice':
            item['durability'] += increase
            item['enchant'] = f"ice {item['name']}"
        case 'lightning':
            item['power'] += increase
            item['enchant'] = f"lightning {item['name']}"
        case _:
            raise ValueError(f"{type} enchantment is not available: " +
                             "only ['fire', 'ice', 'lightning'] available")
    return f"{item['name']}: {type} was incrise by {increase}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """
    Particial: is used to create partial functions, meaning
    that we can fix the values of some arguments and make
    copys of the same fuc but whith those arguments with
    fixed values
    """
    return {
        'fire_enchant': partial(base_enchantment, 50, 'fire'),
        'ice_enchant': partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': partial(base_enchantment, 50, 'lightning')
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Demonstrates the use of Least Recently Used (LRU) caching for optimization.
    The @lru_cache decorator acts as a memory vault (memoization)
    Whenever the function is called, it checks if the result for the given
    argument(s) is already in the cache.
        - If YES (a cache hit): It instantly returns the saved result
        - If NO (a cache miss): It runs the function, calculates the result,
        and saves it in the cache for next time.
    The "LRU" stands for "Least Recently Used." If the cache reaches its
    `maxsize` limit, it will automatically delete the oldest, to make room
    for new ones.
    Primary Use Cases:
    1. Recursive functions that recalculate the same inputs heavily.
    2. Expensive mathematical calculations or data processing.
    3. Web requests or database queries where the data doesn't
    change frequently.
    """
    if n < 2:
        return n
    # The cache intercepts these recursive calls!
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:

    @singledispatch
    def dispatcher(var: Any) -> str:
        return f"Unknown magic type. Cannot dispatch: {var}"

    @dispatcher.register(int)
    def _(demage_spell: int) -> str:
        return f"Spell damge: {demage_spell}"

    @dispatcher.register(str)
    def _(enchantemt: str) -> str:
        return f"{enchantemt} made on the sword"

    @dispatcher.register(list)
    def _(multi_cast: list[str]) -> str:
        return f"{multi_cast} spells cast"
    return dispatcher


def main() -> None:
    values: list[int] = [10, 54, 891, 50, 7]
    print("=== Testing operatrion with reduce() method ===")
    print(f"Original list: {values}")
    print(f"Testing '+': {spell_reducer(values,'add')}")
    print(f"Testing '-': {spell_reducer(values,'sub')}")
    print(f"Testing '*': {spell_reducer(values,'multiply')}")
    print(f"Testing 'max': {spell_reducer(values,'max')}")
    print(f"Testing 'min': {spell_reducer(values,'min')}")
    print(f"Testing 'invalid': {spell_reducer(values,'invalid')}")
    print("\n" + "=" * 55)
    print("=== Testing partial() method for functions ===")
    sword: ITEM = {"name": "sword", "durability": 15,
                   "power": 100, 'enchant': 'just a normal sword'}
    fire = partial_enchanter(enchantment)['fire_enchant']
    ice = partial_enchanter(enchantment)['ice_enchant']
    print("Enchanting the sword ....")
    print(f"Original values item: {sword}")
    print(f"Ice enchantemt: {ice(sword)}")
    print(f"New values: {sword}\n")

    print("Enchanting the shield ....")
    shield: ITEM = {"name": "shield", "durability": 15,
                    "power": 100, 'enchant': 'just a normal sword'}
    print(f"Original values item: {shield}")
    print(f"Fire enchantemt: {fire(shield)}")
    print(f"New values: {shield}\n")

    print("\n" + "=" * 55)
    print("=== Testing lru_cache decorator ===")
    begin = time()
    fibb_seq = memoized_fibonacci(301)
    end = time()
    print(f"300 nbr of fibb sequence: {fibb_seq} in {end-begin:.2f} seconds")
    print(memoized_fibonacci.cache_info())
    print("\n" + "=" * 55)
    print("=== Testing singledispatch decorator ===")
    print("Testing functions with same name but different types ")
    dispatcher = spell_dispatcher()
    print(f"Dispatcher with type (int): {dispatcher(150)}")
    print(f"Dispatcher with type (str): {dispatcher('fire')}")
    print("Dispacher wiht type (list): " +
          f"{dispatcher(['fireball', 'watershield'])}")


if __name__ == "__main__":
    main()
