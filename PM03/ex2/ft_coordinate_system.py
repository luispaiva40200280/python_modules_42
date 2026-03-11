
from sys import argv as argv
from math import sqrt as sqrt


def coord_generator(coordinates: list[str]) -> tuple[int, ...] | None:
    coord: tuple[int, ...]
    if len(coordinates) == 3:
        try:
            coord = tuple(int(cord) for cord in coordinates)
            return coord
        except (IndexError, ValueError) as e:
            raw_val: str = ", ".join(coordinates)
            print(f"Parsing invalid coordinates: \"{raw_val}\"")
            print(f"Error parsing coordinates: {e}")
            print(f"Error details Type: {type(e).__name__}, Args: {e.args}")
    return None


def calc_distance(origin: tuple, destiny: tuple) -> float:
    xo, yo, zo = origin
    xd, yd, zd = destiny
    distance: float = sqrt((xo-xd)**2 + (yo-yd)**2 + (zo-zd)**2)

    return distance


def unpacking_coord(coordinates: list[str]) -> None:
    if len(coordinates) < 6:
        print("Not enough arguments to create the coordinates")
        return

    origin: tuple[int, ...] | None = coord_generator(coordinates[0:3])
    destiny: tuple[int, ...] | None = coord_generator(coordinates[3:6])
    if origin and destiny:
        xp, yp, zp = origin
        distance: float = calc_distance(origin, destiny)
        print(f"Position created: {origin}")
        print(f"Distance between {destiny} and {origin}: {distance:.2f}")
        print()
        print("Unpacking demonstration:")
        print(f"Player at x={xp}, y={yp}, z={zp}")
        print(f"Coordinates: X={xp}, Y={yp}, Z={zp}")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    if len(argv) == 1:
        origin_val: tuple[int, ...] | None = coord_generator(['0', '0', '0'])
        spawn_val: tuple[int, ...] | None = coord_generator(['10', '20', '5'])
        if origin_val and spawn_val:
            dist1: float = calc_distance(origin_val, spawn_val)
        print(f"Position created: {spawn_val}")
        print(f"Distance between {origin_val} and {spawn_val}: {dist1:.2f}\n")
        raw_valid: list[str] = ["3", "4", "0"]
        parsed_pos: tuple[int, ...] | None = coord_generator(raw_valid)
        if parsed_pos and origin_val:
            dist2: float = calc_distance(origin_val, parsed_pos)
            print(f"Parsing coordinates: \"{','.join(raw_valid)}\"")
            print(f"Parsed position: {parsed_pos}")
            print(f"Distance between {origin_val}" +
                  f"and {parsed_pos}: {dist2:.1f}\n")
        raw_invalid: list[str] = ["abc", "def", "ghi"]
        parsed_pos: tuple[int, ...] | None = coord_generator(raw_invalid)
        if parsed_pos:
            xp, yp, zp = parsed_pos
            print("\nUnpacking demonstration:")
            print(f"Player at x={xp}, y={yp}, z={zp}")
            print(f"Coordinates: X={xp}, Y={yp}, Z={zp}")
    else:
        unpacking_coord(argv[1:])


if __name__ == "__main__":
    main()
