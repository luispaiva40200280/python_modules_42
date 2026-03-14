from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime
import json
"""
Pydantic Core Concepts=>
- BaseModel: The foundational Pydantic class. Inheriting from it turns
a standard Python class into a validated data model.
- Field: A function used to add specific validation constraints
(like max length or limits) and default values to model attributes.
- ValidationError: The specific error Pydantic raises when input
data fails to pass the validation rules.
"""


class SpaceStation(BaseModel):
    station_id: str = Field(..., max_length=10, min_length=3)
    name: str = Field(..., max_length=50, min_length=1)
    crew_size: int = Field(..., le=20, ge=1)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200, default=None)

    def __str__(self) -> str:
        status = "Operational" if self.is_operational else "Inoperable"
        return (f"ID: {self.station_id}\n"
                f"Name: {self.name}\n"
                f"Crew: {self.crew_size} people\n"
                f"Power: {self.power_level}%\n"
                f"Oxygen: {self.oxygen_level}%\n"
                f"Status: {status}")


def get_valid_stations() -> list[dict]:
    try:
        with open("space_stations.json", 'r') as file:
            all_valid_stations = json.load(file)
        return all_valid_stations
    except (FileNotFoundError, FileExistsError) as e:
        print(f"Warning: Could not load the JSON file. ({e})")
        return []


def get_invalid_stations() -> list[dict]:
    try:
        with open("invalid_stations.json", 'r') as file:
            all_invalid_stations = json.load(file)
        return all_invalid_stations
    except (FileNotFoundError, FileExistsError) as e:
        print(f"Warning: Could not load the JSON file. ({e})")
        return []


def main() -> None:
    all_valid_stations = get_valid_stations()
    all_invalid_stations = get_invalid_stations()
    if not all_invalid_stations or not all_valid_stations:
        return
    try:
        valid_station = SpaceStation(**all_valid_stations[0])
        print("=" * 55)
        print("Valid station created:")
        print(valid_station)
        print("\n" + ("=" * 55))
        print("Expected validation error:")
        invalid_station = SpaceStation(**all_invalid_stations[0])
        print(invalid_station)
    except ValidationError as err:
        # errr.errors()[0]['msg']
        for e in err.errors():
            print(e['msg'])


if __name__ == "__main__":
    main()
