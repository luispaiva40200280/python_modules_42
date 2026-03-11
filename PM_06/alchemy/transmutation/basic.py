from alchemy.elements import create_fire, create_earth
# from ..elements ....


def lead_to_gold() -> str:
    return ("Lead transmuted to gold using {}"
            .format(create_fire()))


def stone_to_gem() -> str:
    return ("Stone transmuted to gem using {}"
            .format(create_earth()))
