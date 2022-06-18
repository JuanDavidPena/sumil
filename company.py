""" Company model """
from bson import ObjectId
from pydantic import BaseModel, Field, List

from py_object_id import PyObjectId


class Company(BaseModel):
    """ Company model """
    id: PyObjectId = Field(alias='_id')
    name: str
    projects_posted: int
    projects_id: List[ObjectId]

    class Config:  # pylint: disable=too-few-public-methods
        """ Configuration and styling of an instance """
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "example": {
                "name": "Microsoft",
                "projects_posted": 50,
                "projects_id": ["84948459","h923399h"],
            }
        }
