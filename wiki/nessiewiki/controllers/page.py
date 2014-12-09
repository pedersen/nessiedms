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
from webob.exc import HTTPNotFound

# project specific imports
from nessiewiki import model
from nessiewiki.lib.base import BaseController
from nessiewiki.lib.helpers import getlogger
from nessiewiki.model import DBSession

wikiwords = re.compile(r"\b([A-Z]\w+[A-Z]+\w+)")

class PageHistoryController(BaseController):
    """
    TODO: delete specific page revision
    TODO: compare two revisions
    TODO: revert to specific revision
    TODO: display specific revision
    """
    pass

class PageCommentsContgroller(BaseController):
    """
    TODO: add comment
    TODO: delete comment
    TODO: edit comment
    TODO: view comments
    """
    pass

class PageController(BaseController):

    def __init__(self, title, *p, **kw):
        super(PageController, self).__init__()
        log = getlogger(__name__, self.__class__.__name__, '__init__')
        log.debug('title: %s' % (title))
        self.title = title
        self.wp = model.WikiPage.query.find({'title':title}).first()

    @expose()
    def _lookup(self, *p, **kw):
        log = getlogger(__name__, self.__class__.__name__, '_lookup')
        urlmap = {
            'history': None,
            'comments': None
            }
        if p:
            p=list(p)
            url = p.pop(0)
            klass = urlmap.get(url, None)
            if klass:
                return klass(self.wp), p
        raise HTTPNotFound
    
    @expose('nessiewiki.templates.wiki.get_one')
    def index(self, *p, **kw):
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
    def save(self, text, *p, **kw):
        log = getlogger(__name__, self.__class__.__name__, 'save')
        history = model.WikiPageHistory()
        history.page_id = self.wp._id
        history.text = self.wp.text
        self.wp.text = text
        redirect (url('./'))

    @expose()
    def delete(self):
        for h in self.wp.history:
            h.delete()
        for c in self.wp.comments:
            c.delete()
        self.wp.delete()
        redirect(url('../'))
    
    @expose()
    def rename(self, title):
        pass
