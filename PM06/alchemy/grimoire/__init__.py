from .spellbook import record_spell
from .validator import validate_ingredients


__version__ = "1.0.0"
__author__ = "Master Pythonicus"


# This tells Flake8 these imports are intentionally exposed
__all__ = [
    "record_spell",
    "validate_ingredients"
]
