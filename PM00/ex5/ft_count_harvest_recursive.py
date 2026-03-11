def ft_count_harvest_recursive(c: int = 1, d: int | None = None) -> None:
    if d is None:
        d = int(input("Days until harvest: "))
    if c == d:
        print("Days:", c)
        print("Harvest time!")
    else:
        print("Days:", c)
        return ft_count_harvest_recursive(c + 1, d)

# call of the function for testing


ft_count_harvest_recursive()
