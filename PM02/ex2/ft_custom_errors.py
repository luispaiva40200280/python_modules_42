class GardenError(Exception):
    """Base class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related issues."""
    pass


class WaterError(GardenError):
    """Exception raised for watering-related issues."""
    pass


def catch_plant_error() -> str:
    """Tests catching specific custom errors."""
    try:
        plant = "Tomato"
        raise PlantError(f"The {plant} plant is wilting!!")
    except PlantError as e:
        return f"Caught Plant Error: {e}\n"


def catch_water_error() -> str:
    """Tests catching specific custom errors."""
    try:
        raise WaterError("Not enough Water in the tank!!")
    except WaterError as e:
        return f"Caught Water Error: {e}\n"


def catch_garden_error() -> None:
    """Tests that catching GardenError handles all subtypes."""
    plant = "Tomato"
    try:
        raise WaterError("Not enough Water in the tank!!")
    except GardenError as e:
        print(f"cought a Garden Error: {e}")
    try:
        raise PlantError(f"The {plant} plant is wilting!!")
    except GardenError as e:
        print(f"Caught a Garden Error: {e}")


def ft_custom_error() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    print(catch_plant_error())
    print("Testing WaterError...")
    print(catch_water_error())
    print("Testing catching all garden errors...")
    catch_garden_error()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_error()
