from enum import Enum
from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime
from typing import Optional
import json


class ContactType(Enum):
    RADIO = 'radio'
    VISUAL = 'visual'
    PHYSICAL = 'physical'
    TELEPATHIC = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str = Field(..., max_length=15, min_length=5)
    timestamp: datetime
    location: str = Field(max_length=100, min_length=3)
    contact_type: ContactType = Field(...)  # how => join the enum/pydantic
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(le=1440, ge=1)
    witness_count: int = Field(le=100, ge=1)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validator(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type is ContactType.PHYSICAL:
            if not self.is_verified:
                raise ValueError("Physical contact reports must be verified")
        if self.contact_type is ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError("Contact needs atleast 3 witnesses")
        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError("Strong signals (>7.0) should include" +
                                 " received messages")
        return self

    def __str__(self) -> str:
        return (f"ID: {self.contact_id}\n"
                f"Type: {self.contact_type.value}\n"
                f"Location: {self.location}\n"
                f"Signal: {self.signal_strength}/10\n"
                f"Duration: {self.duration_minutes} minutes\n"
                f"Witnesses: {self.witness_count}\n"
                f"Message: {self.message_received}"
                # f"Date of encounter: {self.timestamp}"
                )


def get_alien_contacts() -> list[dict]:
    try:
        with open('alien_contacts.json', 'r') as file:
            valid_contacts = json.load(file)
        return valid_contacts
    except (FileNotFoundError, FileExistsError) as e:
        print(f"Warning: Could not load the JSON file. ({e})")
        return []


def get_invalid_contacts() -> list[dict]:
    try:
        with open('invalid_contacts.json', 'r') as file:
            valid_contacts = json.load(file)
        return valid_contacts
    except (FileNotFoundError, FileExistsError) as e:
        print(f"Warning: Could not load the JSON file. ({e})")
        return []


def main() -> None:
    valid_contacts = get_alien_contacts()
    invalid_contacts = get_invalid_contacts()
    if not valid_contacts or not invalid_contacts:
        return
    try:
        print("=" * 55)
        print("Valid contact report:")
        valid = AlienContact(**valid_contacts[0])
        print(valid)
        # print(valid_contact.model_validate(valid_contact))
    except ValidationError as error:
        for e in error.errors():
            print(f"Error: {e}")
    try:
        print("\n" + "=" * 55)
        print("Expected validation error:")
        invalid = AlienContact(**invalid_contacts[0])
        print(invalid)
    except ValidationError as error:
        for e in error.errors():
            print(f"Error: {e['msg']}")


if __name__ == "__main__":
    main()
