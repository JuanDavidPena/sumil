""" Pets module model """
from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from config.py_object_id import PyObjectId


class Pet(BaseModel):
    """ Pet model """
    id: Optional[PyObjectId] = Field(alias='_id')
    name: str
    vaccination_card: Optional[str]
    additional_observations: Optional[str]
    walk_frequency_per_day: Optional[int]
    bathroom_times: Optional[int]
    bathroom_hours: Optional[list[str]]
    bathroom_type: Optional[str]
    meal_hours: Optional[list[str]]
    diet: Optional[str]
    disabilities: Optional[str]
    health_status: Optional[str]
    prev_surgeries: Optional[str]
    vets_phone: str
    vets_name: str
    breed: Optional[str]
    weight: float
    gender: str
    birth_date: datetime
    type_animal: str
    id_owner: Optional[PyObjectId]
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """ Configuration and styling of an instance """
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "example": {
                "name": "Konga",
                "vaccination_card": "/path/to/image",
                "additional_observations": "Loves to play with kids",
                "walk_frequency_per_day": 4,
                "bathroom_times": 2,
                "bathroom_hours": ["3:00", "6:00", "9:00"],
                "bathroom_type": "Newspaper",
                "meal_hours": ["3:00", "6:00", "9:00"],
                "diet": "She can ony eat her kibbles, never human food",
                "health_status": "Post-operatory",
                "vets_phone": "3017944365",
                "vets_name": "Francisco",
                "weight": 3,
                "gender": "Female",
                "birth_date": "2021-10-16T22:49:37.726Z",
                "type_animal": "Dog"
            }
        }
