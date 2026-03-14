from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
import json


class Rank(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(..., max_length=10, min_length=3)
    name: str = Field(..., max_length=50, min_length=2)
    rank: Rank = Field(...)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(..., max_length=30, min_length=3)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., max_length=15, min_length=5)
    mission_name: str = Field(..., max_length=100, min_length=3)
    destination: str = Field(..., max_length=50, min_length=3)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0,)

    @model_validator(mode='after')
    def validation(self) -> 'SpaceMission':
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")
        cap_or_comd = sum(1 for c in self.crew
                          if c.rank in (Rank.CAPTAIN, Rank.COMMANDER))
        if not cap_or_comd:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            exp_crew = [c for c in self.crew if c.years_experience >= 5]
            if len(exp_crew) < len(self.crew) / 2:
                raise ValueError("Crew is not experienced enough")
        for c in self.crew:
            if not c.is_active:
                raise ValueError("All crew members must be active")
        return self

    def __str__(self) -> str:
        crew_details = ""
        for c in self.crew:
            crew_details += (f"- {c.name.capitalize()} ({c.rank.value}) " +
                             f"- {c.specialization}\n")
        return (f"Mission: {self.mission_name}\n"
                f"ID: {self.mission_id}\n"
                f"Destination: {self.destination}\n"
                f"Duration: {self.duration_days} days\n"
                f"Budget: ${self.budget_millions}M\n"
                f"Crew size: {len(self.crew)}\n"
                f"Crew members:\n"
                f"{crew_details}"
                )


def get_missions() -> list[dict]:
    try:
        with open("space_missions.json", 'r') as file:
            all_missions = json.load(file)
        return all_missions
    except (FileExistsError, FileNotFoundError) as e:
        print(f"Warning: Could not load the JSON file. ({e})")
        return []


def main() -> None:
    missions = get_missions()
    if not missions:
        return
    try:
        print("=" * 55)
        valid = missions[0]
        valid_mision = SpaceMission(**valid)
        print("Valid mission created:")
        print(valid_mision)
    except ValidationError as erros:
        for e in erros.errors():
            print(e)
    try:
        print("=" * 55)
        invalid = missions[1]
        print("Expected validation error:")
        inva_mission = SpaceMission(**invalid)
        print(inva_mission)
    except ValidationError as erros:
        for e in erros.errors():
            print(e['msg'])


if __name__ == "__main__":
    main()
