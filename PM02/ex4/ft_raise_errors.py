def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """Test of the health of the plant"""
    if not isinstance(plant_name, str) or plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if not isinstance(water_level, int) or not (1 <= water_level <= 10):
        raise ValueError(f"Error: Water level {water_level} is invalid")
    if not isinstance(sunlight_hours, int) or not (2 <= sunlight_hours <= 12):
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is invalid")
    else:
        print("Testing good values...")
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("===Garden Plant Health Checker ===\n")
    plant = {"name": "Rose", "water": 8, "sunlight": 10}
    plant_empty_name = {"name": "", "water": 8, "sunlight": 10}
    plant_bad_water = {"name": "Oak", "water": 15, "sunlight": 10}
    plant_sun_hours = {"name": "Lilith", "water": 8, "sunlight": 0}
    plants = [
        plant,
        plant_sun_hours,
        plant_bad_water,
        plant_empty_name
    ]
    for plant in plants:
        try:
            check_plant_health(plant["name"], plant["water"],
                               plant["sunlight"])
        except ValueError as e:
            if 'empty' in str(e):
                print("Testing empty plant name...")
            if plant['water'] > 10:
                print("Testing bad water level...")
            if plant['sunlight'] < 2:
                print("Testing bad sunlight hours......")
            print(e)


if __name__ == "__main__":
    test_plant_checks()
