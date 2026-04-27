from typing import Any


def dummy_data() -> list[Any]:
    artifacts = [{'name': 'Water Chalice', 'power': 97, 'type': 'focus'},
                 {'name': 'Ice Wand', 'power': 118, 'type': 'accessory'},
                 {'name': 'Ice Wand', 'power': 67, 'type': 'focus'},
                 {'name': 'Crystal Orb', 'power': 116, 'type': 'relic'}
                 ]
    mages = [{'name': 'River', 'power': 62, 'element': 'earth'},
             {'name': 'Morgan', 'power': 84, 'element': 'water'},
             {'name': 'Morgan', 'power': 74, 'element': 'lightning'},
             {'name': 'Luna', 'power': 54, 'element': 'earth'},
             {'name': 'River', 'power': 75, 'element': 'earth'}
             ]
    spells = ['shield', 'lightning', 'tornado', 'earthquake']
    return [artifacts, mages, spells]


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda art: art['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    total = sum(map(lambda mag: mag['power'], mages))
    return {
        'max_power': max(mages, key=lambda mag: mag['power'])['power'],
        'min_power': min(mages, key=lambda mag: mag['power'])['power'],
        'avg_power': round(total / len(mages), 2)
    }


def main() -> None:
    artifacts, mages, spells = dummy_data()
    sorted_artifacts = artifact_sorter(artifacts)
    print("=== Artifacts sorted by power (>) ===")
    for nbr, artf in enumerate(sorted_artifacts, start=1):
        print(f"{nbr} - {artf} ")
    print("\n=== Mages filterd by power (> nbr) ===")
    filter_mage = power_filter(mages, 75)
    for nbr, mage in enumerate(filter_mage, start=1):
        print(f"{nbr} - {mage} ")
    print("\n=== Spells name changed ===")
    change_spells = spell_transformer(spells)
    for nbr, spells in enumerate(change_spells, start=1):
        print(f"{nbr} - {spells} ")
    print("\n=== Statistics for mages ===")
    stats_mages = mage_stats(mages)
    for key, val in stats_mages.items():
        print(f"{key} - {val} ")


if __name__ == "__main__":
    main()
