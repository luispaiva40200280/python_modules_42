
def absule_impors() -> None:
    import alchemy.transmutation.basic as basic
    print("Testing Absolute Imports (from basic.py):")
    transmutacions: list = [
        basic.lead_to_gold,
        basic.stone_to_gem,
    ]
    for trans in transmutacions:
        print(f"{trans.__name__}(): {trans()} ")


def relative_imp() -> None:
    from alchemy.transmutation import advanced
    print("\nTesting Relative Imports (from advanced.py):")
    adv_trasns: list = [
        advanced.philosophers_stone,
        advanced.elixir_of_life
    ]
    for adv in adv_trasns:
        print(f"{adv.__name__}(): {adv()}")


def packege_acess() -> None:
    import alchemy.transmutation
    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold(): {}"
          .format(alchemy.transmutation.lead_to_gold()))
    print("alchemy.transmutation.philosophers_stone(): {}"
          .format(alchemy.transmutation.philosophers_stone()))


if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===\n")
    absule_impors()
    relative_imp()
    packege_acess()
    print("\nBoth pathways work! Absolute: clear, Relative: concise")
