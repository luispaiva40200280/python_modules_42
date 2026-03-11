

def validate_ingredients(ingredients: str) -> str:
    # from .spellbook import record_spell  # noqa: F401
    valid = ["fire", "water", "earth", "air"]
    for item in ingredients.split(" "):
        if item not in valid:
            return "INVALID"
    return "VALID"
