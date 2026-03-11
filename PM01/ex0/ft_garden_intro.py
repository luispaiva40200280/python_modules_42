

def main() -> None:
    """
    Initializes plant variables and prints a formatted garden summary
    to the standard output.
    """
    name = "Rose"
    height = "25cm"
    age = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant Name: {name}")
    print(f"Height: {height}")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    """
    Entry Point Check:
    Verifies if this script is being executed directly by the user
    (standard output).
    If True: The script runs the main() function.
    If False: The script was imported as a module, so the main()
    function is skipped
    to prevent unwanted code execution.
    """
    main()
