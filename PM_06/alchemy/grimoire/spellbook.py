

def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    if validate_ingredients(ingredients) == "VALID":
        return ("Spell recorded: {} ({} - {})"
                .format(spell_name, ingredients,
                        validate_ingredients(ingredients)))
    return ("Spell rejected: {} ({} {})"
            .format(spell_name, ingredients,
                    validate_ingredients(ingredients)))
