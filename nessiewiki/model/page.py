# -*- coding: utf-8 -*-
"""Sample model module."""

from ming import schema
from ming.orm import FieldProperty, ForeignIdProperty, RelationProperty
from ming.orm import Mapper
from ming.orm.declarative import MappedClass

from nessiewiki.model import DBSession


class WikiPage(MappedClass):

    class __mongometa__:
        session = DBSession
        name = 'wikipage'
    
    
    _id = FieldProperty(schema.ObjectId)
    title = FieldProperty(str, if_missing='Untitled Page')
    text = FieldProperty(str, if_missing='')

Mapper.compile_all()
