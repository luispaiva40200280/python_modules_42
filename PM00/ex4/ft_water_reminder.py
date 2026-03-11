def ft_water_reminder() -> None:
    days_since_watered = int(input("Enter days since last watered: "))
    if days_since_watered > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

# call of the function for testing
# ft_water_reminder()
