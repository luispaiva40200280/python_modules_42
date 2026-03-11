
def ft_seed_inventory(seed_type: str, quanity: int, units: int) -> None:
    seed_type = seed_type.capitalize()
    if units == "packets":
        print(seed_type + " seeds: " + str(quanity) + " packets available")
    elif units == "grams":
        print(seed_type + " seeds: " + str(quanity) + " grams total")
    elif units == "area":
        print(seed_type + " seeds: covers " + str(quanity) + " square meter")
    else:
        print("Unknown unit type")


# call of the function for testing

"""
ft_seed_inventory("tomato", 15, "packets")
ft_seed_inventory("carrot", 8, "grams")
ft_seed_inventory("lettuce", 12, "area")
"""
