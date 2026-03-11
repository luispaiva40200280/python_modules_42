
class Plant:
    """
    Represents a plant with a name, height, and age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    """
    Manages a garden registry. initializes a list default plants, accepts user
    input for new plants, and prints the final registry.
    """
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    try:
        nunber_of_plants = int(input("HOW MANY PLANTS DO YOU WANT TO ADD:: "))
        if nunber_of_plants <= 0:
            raise ValueError
        for plant in range(nunber_of_plants):
            name = input("Enter plant name: ")
            try:
                height = int(input("Enter plant height (in cm): "))
                age = int(input("Enter plant age (in days): "))
                if age < 0 or height < 0:
                    raise ValueError
                plant = Plant(name, height, age)
                plants.append(plant)
            except ValueError:
                print("ERROR: Height and age must be non-negative integers.")
                break
    except ValueError:
        print("ERROR: Invalid Nunber of plants to add.")
        pass

    print("\n=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height} cm, {plant.age} days")


if __name__ == "__main__":
    ft_garden_data()
