""" Project model """
from bson import ObjectId
from pydantic import BaseModel, Field, List

from py_object_id import PyObjectId


class Project(BaseModel):
    """ Project model """
    id: PyObjectId = Field(alias='_id')
    name: str
    url: str
    difficulty: int
    closing_date: str
    amount_people: int
    amount_rewards: int
    reward_type: str
    suscribers_id: List[str]
    projects_id: List[ObjectId]

    class Config:  # pylint: disable=too-few-public-methods
        """ Configuration and styling of an instance """
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "example": {
                "name": "Project NEAR development",
                "project": "https://github.com/adri-er/sorting_algorithms/blob/main/README.md",
                "difficulty": 3,
                "closing_date":"03-08-2024",
                "amount_people": 15,
                "reward_amount": 4500,
                "reward_type":"USD",
                "suscribers_id":["1048593ff98","1038383988k","038os494933"]
            }
        }
