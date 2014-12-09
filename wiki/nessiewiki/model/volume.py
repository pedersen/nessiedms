# -*- coding: utf-8 -*-
"""Volume model module."""

from ming import schema
from ming.orm import FieldProperty, ForeignIdProperty, RelationProperty
from ming.orm import Mapper
from ming.orm.declarative import MappedClass

from nessiewiki.model import DBSession


class Volume(MappedClass):

    class __mongometa__:
        session = DBSession
        name = 'volume'
    
    
    _id = FieldProperty(schema.ObjectId)
    name = FieldProperty(str)
    pages = RelationProperty('WikiPage')

Mapper.compile_all()
