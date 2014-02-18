# -*- coding: utf-8 -*-
"""Sample model module."""

from datetime import datetime
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

    history = RelationProperty('WikiPageHistory')
    comments = RelationProperty('WikiPageComment')

class WikiPageHistory(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'wikipage_history'

    _id = FieldProperty(schema.ObjectId)
    page_id = ForeignIdProperty('WikiPage')
    title = FieldProperty(str, if_missing='Untitled Page')
    text = FieldProperty(str, if_missing='')
    saveddate = FieldProperty(datetime, if_missing=datetime.utcnow)

    page = RelationProperty('WikiPage')

class WikiPageComment(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'wikipage_comment'

    _id = FieldProperty(schema.ObjectId)
    page_id = ForeignIdProperty('WikiPage')
    text = FieldProperty(str, if_missing='')
    saveddate = FieldProperty(datetime, if_missing=datetime.utcnow)

    page = RelationProperty('WikiPage')
    
Mapper.compile_all()
