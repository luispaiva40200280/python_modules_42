
class Plant:
    """
    Represents a plant with tracking for height and age.
    """
    def __init__(self, name: str, height: int = 5, age: int = 1) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return (f"Created: {self.name.capitalize()}: ({self.height}"
                f"cm, {self.age} days)"
                )


def ft_plant_factory() -> None:
    """
    Creates multiple plant objects based on user input and displays
    the factory output.
    """
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    for _ in range(1):
        try:
            name = input("Enter plant name: ")
            if not name:
                raise ValueError("the name cant be empty")
            height = int(input("Enter plant height (in cm): ") or 0)
            age = int(input("Enter plant age (in days): ") or 0)
            if age < 0 or height < 0:
                raise ValueError("Height or age must be non-negative integers")
            plant = Plant(name, height, age)
            plants.append(plant)
            print(f"\n--- Plant {name} Created ---\n")
        except ValueError as e:
            print(f"ERROR: {e}")
            print("Plant was not created")
    print("\n=== Plant Factory Output  ===")
    for plant in plants:
        print(plant)
    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    ft_plant_factory()
