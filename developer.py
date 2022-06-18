""" Developer model """
from bson import ObjectId
from pydantic import BaseModel, Field, List

from py_object_id import PyObjectId


class Developer(BaseModel):
    """ Developer model """
    id: PyObjectId = Field(alias='_id')
    name: str
    skills: List[str]
    points: int
    github: str
    amount_projects: int

    class Config:  # pylint: disable=too-few-public-methods
        """ Configuration and styling of an instance """
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "example": {
                "name": "Jhon",
                "skills": ["php", "java", "python"],
                "points": 450,
                "github": "https://github.com/adri-er",
                "amount_projects": 10
            }
        }
