
def check_temperature(temp_str: str) -> int | None:
    """Validates if the input string is a valid agricultural temperature."""
    try:
        temp = int(temp_str)
        if temp > 40:
            print(f"{temp}˚C is too hot for the plants\n")
            return
        elif temp < 0:
            print(f"{temp}˚C is too cold for the plants\n")
            return
        else:
            print(f"Temperature {temp}˚C is perfect for plants!\n")
            return temp
    except ValueError:
        print(f"Error {temp_str} is not valid number\n")
        return


def test_temperature_input() -> None:
    """Demonstrates various temperature scenarios
    as required by the subject."""
    print("=== Garden Temperature Checker ===\n")
    print("testing temperature: 25")
    check_temperature("25")

    print("testing temperature: abc")
    check_temperature("abc")

    print("testing temperature: 100")
    check_temperature("100")

    print("testing temperature: -50")
    check_temperature("-50")

    print("All tests completed\n" +
          "program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
