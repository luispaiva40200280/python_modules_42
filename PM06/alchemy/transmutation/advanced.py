from ..potions import healing_potion as heal
from .basic import lead_to_gold


def philosophers_stone() -> str:
    return ("Philosopher’s stone created using {} {}"
            .format(lead_to_gold(), heal()))


def elixir_of_life() -> str:
    return "elixir of life: eternal youth achieved!"
