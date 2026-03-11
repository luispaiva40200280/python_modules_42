
def ft_count_harvest_iterative() -> None:
    days_to_harvest = int(input("Days until harvest: "))
    count = 0
    while count < days_to_harvest:
        print("Days:", count + 1)
        count += 1
    if count == days_to_harvest:
        print("Harvest time!")

# call of the function for testing


ft_count_harvest_iterative()
