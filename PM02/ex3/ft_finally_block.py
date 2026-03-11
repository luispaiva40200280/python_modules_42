
def water_plants(plant_list: list) -> None:
    """
        :param plant_list: list of all the plants to water
        :type plant_list: list
    """
    print("Open watering system")
    try:
        for plant in plant_list:
            if not isinstance(plant, str):
                raise TypeError
            else:
                print(f"Watering {plant}")
    except TypeError:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Close of the watering system (cleanup)")


def test_watering_system() -> None:
    """Call of the watering system on a valid and invalid list"""
    print("=== Garden Watering System ===")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print()
    print("Testing with error...")
    water_plants(["tomato", None, "lettuce"])
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
