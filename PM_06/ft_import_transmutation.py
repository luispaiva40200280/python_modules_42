
def method_one() -> None:
    import alchemy.elements   # importing all potions
    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire(): {}\n"
          .format(alchemy.elements.create_fire()))


def method_two() -> None:
    from alchemy.elements import create_water
    print("Method 2 - Specific function import:")
    print("create_water(): {}\n"
          .format(create_water()))


def method_three() -> None:
    from alchemy.potions import healing_potion as heal
    print("Method 3 - Aliased import:")
    print("heal(): {}\n"
          .format(heal()))


def method_four() -> None:
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion
    elements_lst: list = [
        create_fire,
        create_earth,
        strength_potion
    ]
    for elem in elements_lst:
        print(f"{elem.__name__}(): {elem()}")


if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===\n")
    method_one()
    method_two()
    method_three()
    method_four()
    print()
    print("All import transmutation methods mastered!")
