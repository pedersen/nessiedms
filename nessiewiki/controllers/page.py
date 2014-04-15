# -*- coding: utf-8 -*-
"""Page controller module"""

import re
import urllib

from docutils.core import publish_parts

# turbogears imports
from tg import expose, url

from tg import redirect, validate, flash
#from tg.i18n import ugettext as _
#from tg import predicates

# project specific imports
from nessiewiki import model
from nessiewiki.lib.base import BaseController
from nessiewiki.lib.helpers import getlogger
from nessiewiki.model import DBSession

wikiwords = re.compile(r"\b([A-Z]\w+[A-Z]+\w+)")

class PageController(object):

    def __init__(self, title, *p, **kw):
        log = getlogger(__name__, self.__class__.__name__, '__init__')
        log.debug('title: %s' % (title))
        self.title = title
        self.wp = model.WikiPage.query.find({'title':title}).first()
        
    @expose('nessiewiki.templates.wiki.get_one')
    def _default(self, *p, **kw):
        if self.wp is None:
            redirect(url('./%s/edit' % self.title))
        content = publish_parts(self.wp.text, writer_name="html")["html_body"]
        root = url('/')
        content = wikiwords.sub(r'<a href="%s\1">\1</a>' % root, content)

        return {'pagetitle': self.wp.title, 'content': content}

    @expose('nessiewiki.templates.wiki.edit')
    def edit(self, *p, **kw):
        if self.wp is None:
            self.wp = model.WikiPage(title=self.title)
            DBSession.flush()
        return {'page': self.wp}

    @expose()
    def save(self, title, text, *p, **kw):
        log = getlogger(__name__, self.__class__.__name__, 'save')
        history = model.WikiPageHistory()
        history.page_id = self.wp._id
        history.title = self.wp.title
        history.text = self.wp.text
        self.wp.text = text
        self.wp.title = title
        redirect (url('./'))

    @expose()
    def rename(self, title):
        pass

    @expose()
    def delete(self):
        self.wp.delete()
        redirect(url('../'))
    
        
