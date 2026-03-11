
class Plant:
    """
    A base class representing a generic plant in the garden.

    Attributes:
        name (str): The common name of the plant.
        height (int): The current height of the plant in cm.
        age (int): The age of the plant in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new Plant instance."""
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        """Return a string representation of the plant."""
        return f"{self.name}: {self.height}cm tall, {self.age} days old"


# start the child classes to add plant types
class Flower(Plant):
    """
    Represents a flowering plant, inheriting from Plant.

    Attributes:
        color (str): The color of the flower's petals.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return f"{self.name} is blooming with {self.color} flowers!"


class Tree(Plant):
    """
    Represents a tree, inheriting from Plant, with trunk measurements.

    Attributes:
        trunk_diameter (int): The diameter of the tree trunk in cm.
    """
    def __init__(self, name: str,
                 height: int, age: int, diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = diameter

    def produce_shade(self) -> str:
        shade_area = int(self.trunk_diameter * 0.14)
        return f"{self.name} is providing {shade_area} square meters"


class Vegetable(Plant):
    """
    Represents an edible plant, inheriting from Plant.

    Attributes:
        nutritional_value (int): The calorie count or nutritional score.
        harvest_season (str): The season when the vegetable is ready to
        harvest.
    """
    def __init__(self, name: str,
                 height: int, age: int,
                 nutricinal_value: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.nutricinal_value = nutricinal_value
        self.harvest_season = harvest_season

    def get_atributes(self) -> str:
        return (f"{self.nutricinal_value} calories, harvested in "
                + f"{self.harvest_season}")


def main() -> None:
    """
    Orchestrates the garden simulation.
    Initializes lists of specific plant types (Flowers, Trees, Vegetables),
    iterates through each category, and prints their status and unique
    behaviors to the standard output.
    """
    roses = [Flower("Rose", 50, 30, "red"),
             Flower("Tulip", 40, 20, "yellow")]
    oaks = [Tree("Oak", 500, 100, 120),
            Tree("Pine", 600, 80, 100)]
    Vegetables = [Vegetable("Carrot", 30, 60, 41, "Summer"),
                  Vegetable("Lettuce", 25, 45, 15, "Spring")]

    for flower in roses:
        print(flower)
        print(flower.bloom() + "\n")
    for tree in oaks:
        print(tree)
        print(tree.produce_shade() + "\n")
    for veg in Vegetables:
        print(veg)
        print(veg.get_atributes() + "\n")


if __name__ == "__main__":
    main()
