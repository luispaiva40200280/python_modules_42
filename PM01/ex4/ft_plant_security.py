class SecurePlant:
    """
    A plant class that validates data to ensure no negative values exist.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: int) -> str:
        if height < 0:
            return (
                f"Invalid operation attempted: height {height}cm [REJECTED]\n"
                + "Security: Negative height rejected!"
            )
        else:
            self._height = height
            return f"Height updated: {height}cm [OK]."

    def set_age(self, age: int) -> str:
        if age < 0:
            return (
                f"Invalid operation attempted: age {age} days [REJECTED]\n"
                + "Security: Negative age rejected!"
            )
        else:
            self._age = age
            return f"Age updated: {age} days [OK]."


def get_plant_info() -> None:
    try:
        name = input("Enter plant name: ").capitalize()
        if not name or name.isdigit():
            raise ValueError("The name is invalid")
        height = int(input("Enter plant height in cm: "))
        age = int(input("Enter plant age in days: "))
        if not age or not height:
            raise ValueError("Height and age must be positive integers.")
    except ValueError as e:
        if "invalid literal" in str(e):
            print("Error: Height and age must be positive integers.")
        else:
            print(f"ERROR: {e}.")
        return
    plant = SecurePlant(name, height, age)
    print("\n== Garden Security System ==")
    print(plant.set_height(height))
    print(plant.set_age(age))
    if height >= 0 and age >= 0:
        print(f"\nCurrent plant: {plant.get_name()} ({plant.get_height()}cm, "
              f"{plant.get_age()} days)")


if __name__ == "__main__":
    get_plant_info()
