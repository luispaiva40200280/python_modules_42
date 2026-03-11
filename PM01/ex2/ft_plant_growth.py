
class Plant:
    """
    Represents a plant with tracking for height and age.
    """
    def __init__(self, name: str, height: int, lifetime: int) -> None:
        self.name = name
        self.height = height
        self.lifetime = lifetime

    """adds +1 cm for the initial hight of the plant"""
    def grow(self) -> None:
        self.height += 1

    """adds +1 day for the initial age of the plant"""
    def age(self) -> None:
        self.lifetime += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.lifetime} days old"


def ft_plant_growth() -> None:
    """
    Simulates plant growth over a period of 7 days.
    Updates height and age daily and prints the status.
    """
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    i = 1
    print(f"=== Day {i} ===")
    inicial_info = plants[0].get_info()
    inicial_height = plants[0].height
    print(inicial_info)  
    while i < 7:
        for plant in plants:
            plant.grow()
            plant.age()
        i += 1
    final_info = plants[0].get_info()
    final_height = plants[0].height
    growth = final_height - inicial_height
    print(f"=== Day {i} ===")
    print(final_info)
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
