class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water: int, health: int) -> None:
        self.name = name
        self.water = water
        self.health = health


class GardenManager:
    """""
    Orchestrates agricultural data monitoring and fault-tolerant operations.
    This class integrates error handling techniques to ensure data integrity
    under real-world farming conditions.
    """
    def __init__(self):
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        try:
            if not plant.name:
                raise ValueError("Plant name cannot be empty!")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except ValueError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                try:
                    print(f"Watering {plant.name}")
                    if plant.water < 0:
                        plant.health = 0
                        raise WaterError("Water level is too low"
                                         + f"for {plant.name}")
                    while plant.water < 6:
                        plant.water += 1
                except WaterError as e:
                    print(f"Caught WaterError: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self) -> None:
        print("Checking plant health...")
        for plant in self.plants:
            try:
                if plant.health < 3:
                    raise PlantError(f"{plant.name} is wilting!")
                if plant.water > 10:
                    raise WaterError(f"Water level {plant.water} is too high"
                                     + f" for {plant.name}")
                print(f"{plant.name}: healthy")
            except GardenError as e:
                print(f"Error checking {plant.name}: {e}")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    manager = GardenManager()
    p1 = Plant("Tomato", 5, 10)
    p3 = Plant("rose", -10, 10)
    p2 = Plant("", 5, 10)
    manager.add_plant(p1)
    manager.add_plant(p2)
    manager.add_plant(p3)
    manager.water_plants()
    p3 = Plant("DeadFlower", 5, 1)
    manager.add_plant(p3)
    manager.check_plant_health()
    print("\nGarden management system test complete!")
