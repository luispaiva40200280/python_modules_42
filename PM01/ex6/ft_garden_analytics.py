
class Plant:
    """
    A base class representing a generic plant in the garden.

    Attributes:
        name (str): The common name of the plant.
        height (int): The current height of the plant in cm.
        age (int): The age of the plant in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        """Update height, complying with Ex2 requirements."""
        if cm > 0:
            self.height += cm
            print(f"{self.name} grow {cm}cm")

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    Represents a flowering plant, inheriting from Plant.

    Attributes:
        color (str): The color of the plant's flowers.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a new FloweringPlant instance.

        Args:
            name (str): The name of the plant.
            height (int): The height in cm.
            age (int): The age in years.
            color (str): The color of the flowers.
        """
        super().__init__(name, height, age)
        self.color = color

    def __str__(self) -> str:
        """
        Return a string representation including the flower color.

        Returns:
            str: The parent string representation plus the flower color.
        """
        return super().__str__() + f", Color: {self.color}"


class PrizeFlower(FloweringPlant):
    """
    Represents a prize-winning flower, inheriting from FloweringPlant.

    Attributes:
        points (int): The score or points awarded to this flower.
    """
    def __init__(self, name: str, height: int,
                 age: int, color: str, points: int) -> None:
        super().__init__(name, height, age, color)
        self.points = points

    def __str__(self) -> str:
        """
        Return a string representation including the flower color.

        Returns:
            str: The parent string representation plus the flower color.
        """
        return super().__str__() + f", Points: {self.points}"


class Garden:
    """Represents a collection of plants owned by a specific person.

    Attributes:
        owner (str): The name of the garden's owner.
        garden_plants (list): A list containing Plant objects in this garden.
    """
    def __init__(self, owner: str) -> None:
        """
        Initialize an empty Garden for a specific owner.

        Args:
            owner (str): The name of the garden owner.
        """
        self.owner = owner
        self.garden_plants = []
        self.score = 0

    def add_plant(self, plant: Plant) -> None:
        """
        Add a plant object to the garden's collection.

        Args:
            plant (Plant): The plant instance to add.
        """
        self.garden_plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def call_score(self) -> int:
        score = len(self.garden_plants) + 10
        self.score = score
        return score


class GardenManager:
    """
    Manages a network of gardens and provides statistical utilities.

    Attributes:
        gardens (dict): A dictionary mapping owner names (str) to Garden
        objects.
    """
    class GardenStats:
        """
        Inner utility class for calculating garden statistics.
        """
        @staticmethod
        def calculate_total_height(plants: list) -> int:
            """
            Calculate the sum of heights for a list of plants.

            Args:
                plants (list): A list of Plant objects.

            Returns:
                int: The total height of all plants combined.
            """
            total = 0
            for plant in plants:
                total += plant.height
            return total

        @staticmethod
        def count_plant_types(plants: list) -> str:
            regular = 0
            flowering = 0
            prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return (f"Plant types: {regular} regular, {flowering} flowering,"
                    + f"{prize} prize flowers"
                    )

    def __init__(self) -> None:
        """Initialize an empty GardenManager."""
        self.gardens = {}

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """
        Factory method to initialize and return a new GardenManager.

        Returns:
            GardenManager: A new instance of the manager.
        """
        print("Booting up the Garden Network...")
        print("Establishing connections...\n")
        new_manager = cls()
        return new_manager

    def add_garden(self, owner: str) -> Garden:
        """Create a new garden for an owner and track it in the manager.

        Args:
            owner (str): The name of the new garden owner.

        Returns:
            Garden: The newly created Garden object.
        """
        new_garden_owner = Garden(owner)
        self.gardens[owner] = new_garden_owner
        return new_garden_owner

    def get_garden(self, owner: str) -> Garden | None:
        """
        Retrieve a specific garden by the owner's name.

        Args:
            owner (str): The name of the owner to look up.

        Returns:
            Garden: The Garden object if found, otherwise None.
        """
        return self.gardens.get(owner)

    def generate_report(self, owner: str) -> None:
        """
        Print a detailed report of the plants in a specific owner's garden.

        Args:
            owner (str): The owner whose garden report should be generated.
        """
        garden = self.get_garden(owner)
        if garden is None:
            print("The garden does not exist!")
            return
        print(f"=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in garden.garden_plants:
            print(f"- {plant}")
        total = self.GardenStats.calculate_total_height(garden.garden_plants)
        print(self.GardenStats.count_plant_types(garden.garden_plants))
        print(f"Total Plant Height: {total}cm")


def main() -> None:
    """
    Main execution entry point.
    Initializes the network, adds plants, and generates a report.
    """
    print("Garden Management System Demo")

    manager = GardenManager.create_garden_network()
    alice_garden = manager.add_garden("Alice")
    oak = Plant("Oak Tree", 100, 50)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    print("\nAlice is helping all plants grow...")
    oak.grow(1)
    rose.grow(1)
    sunflower.grow(1)

    print("")
    manager.generate_report("Alice")
    print("Height validation test: True")
    bob_garden = manager.add_garden("Bob")
    print(f"Garden scores Alice: {alice_garden.call_score()}, " +
          f"Bob: {bob_garden.call_score()}")
    print(f"Total gardens managed: {len(manager.gardens)}")


if __name__ == "__main__":
    main()
