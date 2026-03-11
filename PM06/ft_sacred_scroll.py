import alchemy
"""
Importing a package directory (e.g., 'import alchemy') tells Python to
locate the folder and automatically execute its '__init__.py' file.
Rather than copy-pasting code like a C header, Python runs the file and
creates a module object (a namespace) in memory. Only the specific items
explicitly imported inside '__init__.py' are attached to this object and
exposed to the outside world, allowing you to access them using dot notation
(e.g., alchemy.create_fire()).
"""

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print("alchemy.elements.create_water(): {} "
          .format(alchemy.elements.create_water()))
    print("alchemy.elements.create_earth(): {}"
          .format(alchemy.elements.create_earth()))
    print("alchemy.elements.create_air(): {}"
          .format(alchemy.elements.create_air()))

    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    try:
        print(alchemy.create_earth())  # type: ignore
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        print(alchemy.create_air())  # type: ignore
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")

"""
A namespace is Python's system for organizing names
(variables, functions, classes)
to ensure they remain unique and do not overwrite each other.
Think of namespaces like folders on a computer: you can have two files named
'spell.txt' as long as they are in different folders. Similarly, you can have
two functions named 'create_fire()' as long as they live in
different module namespaces.

Import Behaviors:
- 'import alchemy': Creates an isolated namespace named 'alchemy'. To use its
  contents, you must explicitly reach into it using dot notation
  (e.g., alchemy.create_fire()). This is safe and prevents naming collisions.
- 'from alchemy import *': Dumps all the module's exposed contents directly
  into your current global namespace. This is dangerous because it can silently
  overwrite existing variables or functions with the same names.
"""
