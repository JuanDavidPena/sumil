""" object id module"""
from bson import ObjectId


class PyObjectId(ObjectId):
    """ Object Id encoder """

    @classmethod
    def _get_validators_(cls):
        """ yield validations"""
        yield cls.validate

    @classmethod
    def validate(cls, value):
        """validate object id"""
        if not ObjectId.is_valid(value):
            raise ValueError('Invalid object id')
        return ObjectId(value)

    @classmethod
    def _modify_schema_(cls, field_schema):
        """ transform to string """
        field_schema.update(type='string')
