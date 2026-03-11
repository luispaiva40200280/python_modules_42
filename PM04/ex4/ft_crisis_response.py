def ft_crisis_response(file_name: str) -> None:
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    try:
        if "classified" in file_name:
            raise PermissionError("Security protocols deny access")
        with open(file_name, "r") as file:
            # If we get here, the file opened successfully!
            print("RESPONSE: Archive recovered 'Knowledge preserved for "
                  + "humanity'")
            file.read()
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: Unexpected anomaly: {e}")
        print("STATUS: System reset required")


def main():
    print("=== CYBER ARCHIVES CRISIS RESPONSE SYSTEM ===\n")
    # Test Scenario 1: The Missing File
    ft_crisis_response("lost_archive.txt")
    print()
    # Test Scenario 2: The Forbidden File
    ft_crisis_response("classified_vault.txt")
    print()
    # Test Scenario 3: The Valid File
    ft_crisis_response("standard_archive.txt")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
