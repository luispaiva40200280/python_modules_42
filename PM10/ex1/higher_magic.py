from typing import Callable, Any
from itertools import pairwise


def dummy_fireball(*args: Any, **kwargs) -> str:
    return f"Fireball hits {args}"


def dummy_heal(*args: Any, **kwargs) -> str:
    return f"Heals {args}"


def base_spell(*args, **knargs: Any) -> int:
    power = knargs['power']
    return power


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """*args=> tupple tha as the same type of data
        **kwargs=> is a dictionary with keys an values
        """
    def combine(*args: Any, **kwargs: Any) -> tuple:
        first = spell1(*args, **kwargs)
        scond = spell2(*args, **kwargs)
        return (first, scond)

    return combine


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args: Any, **kwargs: Any) -> int:
        original_power = base_spell(*args, **kwargs)
        return original_power * multiplier

    return amplified


def dummy_spell(*args: Any, **kwargs: Any) -> str:
    return (f"{kwargs['name']} spell cast with {kwargs['power']} of power"
            f"and cost: {kwargs['mana']} ")


def condition_spell(*args: Any, **kwargs: Any) -> bool:
    mana = int(args[0])
    if not mana or mana < kwargs['mana']:
        return False
    return True


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(*args: Any, **kwargs: Any) -> Any:
        if not condition(*args, **kwargs):
            return "Spell fizzled"
        return spell(*args, **kwargs)
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs) -> list[str]:
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


def main() -> None:
    print("=== Spell Combiner using hiarchy on functions ===")
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    comb_spell = spell_combiner(dummy_fireball, dummy_heal)
    for target, nex_target in pairwise(test_targets):
        result = comb_spell(target, nex_target)
        print(f"Target: {target, nex_target} -> Result: {result}")
    print()
    print("=== Spell Amplifier using hiarchy on functions ===")
    fireball = {'name': 'fireball', 'power': 2, 'mana': 5}
    spell = base_spell(**fireball)
    print(f"Original spell: {fireball['name']} (original power {spell})")
    multiplier = 5
    fireball_amplifier = power_amplifier(
        base_spell, multiplier)
    print(f"Spell {fireball['name']} by amplifeid {multiplier}")
    print(f"Amplified power: {fireball_amplifier(**fireball)}")
    print()
    print("=== Casting Spells condicionaly using hiarchy on functions ===")
    caster = conditional_caster(condition_spell, dummy_spell)
    waterball = {'name': 'waterball', 'power': 2, 'mana': 5}
    print(f"Needs {waterball['mana']} of mana to be cast ")
    print("Cast sepll with a condicion: " +
          f"{caster(1, **waterball)}")
    print("=== Casting various Spells using hiarchy on functions ===")
    print()
    seq_caster = spell_sequence(
        [dummy_fireball, dummy_heal, dummy_spell])
    combo = seq_caster(test_targets, **waterball)
    print("Sequenc of spells:")
    for nbr, spell in enumerate(combo, 1):
        print(f"{nbr} - {spell} ")


if __name__ == "__main__":
    main()
