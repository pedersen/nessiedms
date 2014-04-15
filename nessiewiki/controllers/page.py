# -*- coding: utf-8 -*-
"""Page controller module"""

# turbogears imports
from tg import expose

#from tg import redirect, validate, flash
#from tg.i18n import ugettext as _
#from tg import predicates

# project specific imports
from nessiewiki.lib.base import BaseController
#from nessiewiki.model import DBSession, metadata


class PageController(BaseController):

    @expose()
    def _default(self, *p, **kw):
        pass
    
    @expose('nessiewiki.templates.index')
    def index(self):
        return dict(page='index')

