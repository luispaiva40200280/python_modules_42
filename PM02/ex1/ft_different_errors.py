
def test_error_types() -> None:
    """Demonstrates different error types."""
    print("Testing ValueError...")
    try:
        test_int = int("abc")
        print(f"{test_int} is a int")
    except ValueError as e:
        print(f"The input user is not a number: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        nub1 = int('abc')
        nub2 = 0
        division = nub1 / nub2
        print(f"the {nub1} / {nub2} == {division} ")
    except (ZeroDivisionError, ValueError) as e:
        print("Inpossible to divide the numbers: "
              + f"ERROR: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        fd = "ola.txt"
        file_test = open(fd)
        print(f"{fd} was open")
        file_test.close()
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{fd}'\n")

    print("Testing KeyError...")
    try:
        plants = {
            "rose": "Red Flower",
            "tulip": "Pink Flower",
            "sunflower": "Yellow Flower"
            }
        plant = "ro"
        print(f"Plant to see: {plant}")
        print(f"Info: {plants[plant]}")
    except KeyError:
        print(f"Caught KeyError: missing: {plant}\n")


if __name__ == "__main__":
    print("===  Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")
