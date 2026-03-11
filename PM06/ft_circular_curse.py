import alchemy.grimoire as spells


def test_ing_valid() -> None:
    print("Testing ingredient validation:")
    valid_ingrid = "fire air"
    invalid_ingrid = "dragons scales"
    print("validate_ingredients(\"fire air\") {} {}"
          .format(valid_ingrid, spells.validate_ingredients(valid_ingrid)))
    print("validate_ingredients(\"dragons scale\") {} {}"
          .format(invalid_ingrid, spells.validate_ingredients(invalid_ingrid)))


def spell_record_valid() -> None:
    print("\nTesting spell recording with validation:")
    print("record_spell(\"Fireball\", \"fire air\"): {}"
          .format(spells.record_spell("Fireball", "fire air")))
    print("record_spell(\"Dark Magic\", \"shadow\"): {}"
          .format(spells.record_spell("Dark Magic", "shadow")))


def late_imp() -> None:
    print("\nTesting late import technique:")
    print("record_spell(\"Lightning\", \"air\"): {}"
          .format(spells.record_spell("Lightning", "air")))


if __name__ == "__main__":
    print("=== Circular Curse Breaking ===\n")
    test_ing_valid()
    spell_record_valid()
    late_imp()
    print()
    print("Circular dependency curse avoided using late imports!\n" +
          "All spells processed safely!\n")
