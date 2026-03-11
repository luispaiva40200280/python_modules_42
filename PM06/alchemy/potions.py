def healing_potion() -> str:
    # Importing specifically inside the  as requested
    from .elements import create_fire, create_water
    return ("Healing potion brewed with {} and {}"
            .format(create_fire(), create_water()))


def strength_potion() -> str:
    from .elements import create_earth, create_fire
    return ("Strength potion brewed with {} and {}"
            .format(create_earth(), create_fire()))


def invisibility_potion() -> str:
    from .elements import create_air, create_water
    return ("Invisibility potion brewed with {} and {}"
            .format(create_air(), create_water()))


def wisdom_potion() -> str:
    from .elements import create_fire, create_water, create_earth, create_air
    all_results = [create_fire(),
                   create_water(),
                   create_earth(),
                   create_air()]
    return f"Wisdom potion brewed with all elements: {', '.join(all_results)}"
