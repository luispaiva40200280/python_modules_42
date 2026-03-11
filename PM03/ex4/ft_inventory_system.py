from sys import argv as argv


def demo() -> None:
    """Create the dictionary with demo data """
    inventory = {
        "sword": 1,
        "potion": 5,
        "shield": 2,
        "armor": 3,
        "helmet": 1
    }
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    check = "sword" in inventory
    print(f"Sample lookup - 'sword' in inventory: {check}")


def init_inventory(argv: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for a in argv:
        try:
            item_values: list[str] = a.split(":")
            if len(item_values) != 2:
                continue
            name: str = item_values[0].capitalize()
            count: int = int(item_values[1])
            if name in inventory:
                inventory[name] += count
            else:
                inventory[name] = count
        except (ValueError, IndexError) as e:
            print(f"Error parsing '{a}': {e}")
    return inventory


def main() -> None:
    inventory: dict[str, int] = init_inventory(argv[1:])
    if not inventory:
        demo()
        return
    print("=== Inventory System Analysis ===")
    unique: int = len(inventory.keys())
    total: int = sum(inventory.values())
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {unique}")
    print("\n=== Current Inventory ===")
    for item in inventory.items():
        name, count = item
        percentage: float = (count / total) * 100
        print(f"{name}: {count} units ({percentage:.1f}%)")
    print("\n=== Inventory Statistics ===")
    most_count: int = max(inventory.values())
    most_name: str
    for item in inventory.items():
        name, count = item
        if most_count == count:
            most_name = name
    print(f"Most abundant: {most_name} ({most_count})")
    least_count: int = min(inventory.values())
    least_name: str
    for item in inventory.items():
        name, count = item
        if least_count == count:
            least_name = name
    print(f"Least abundant: {least_name} ({least_count})")
    print("\n=== Item Categories ===")
    scarce: dict[str, int] = {
        name: count for name, count in inventory.items() if count < 5
        }
    moderate: dict[str, int] = {
        name: count for name, count in inventory.items() if 5 <= count < 10
        }
    abundant: dict[str, int] = {
        name: count for name, count in inventory.items() if count >= 10
        }
    if abundant:
        print(f"Abundant: {abundant}")
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")
    print("\n=== Management Suggestions ===")
    restock: dict[str, int] = {
        name: count for name, count in inventory.items() if count <= 1
        }
    if restock:
        print(f"Restock needed: {restock}")
    sell: dict[str, int] = {
        name: count for name, count in inventory.items() if count >= 8
        }
    if sell:
        print(f"Sell some of those items: {sell}")


if __name__ == "__main__":
    if len(argv) == 1:
        demo()
    else:
        main()
