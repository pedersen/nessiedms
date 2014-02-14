# -*- coding: utf-8 -*-
"""Main Controller"""

import re
import urllib

from bson.objectid import ObjectId
from docutils.core import publish_parts
from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg import predicates
from tgext.admin.mongo import TGMongoAdminConfig
from tgext.admin.controller import AdminController

from nessiewiki.lib.base import BaseController
from nessiewiki.lib.helpers import getlogger
from nessiewiki import model
from nessiewiki.controllers.error import ErrorController

__all__ = ['RootController']

wikiwords = re.compile(r"\b([A-Z]\w+[A-Z]+\w+)")

class RootController(BaseController):
    """
    The root controller for the nessiewiki application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    admin = AdminController(model, None, config_type=TGMongoAdminConfig)

    error = ErrorController()

    @expose('nessiewiki.templates.wiki.get_one')
    def _default(self, *p, **kw):
        log = getlogger(__name__, self.__class__.__name__, '_default')
        title = '/'.join(p)
        log.debug('title: %s' % (title))
        wp = model.WikiPage.query.get(title=title)
        content = publish_parts(wp.text, writer_name="html")["html_body"]
        root = url('/')
        content = wikiwords.sub(r'<a href="%s\1">\1</a>' % root, content)

        return {'pagetitle': wp.title, 'content': content, '_id': wp._id}

    @expose('nessiewiki.templates.wiki.edit')
    def edit(self, _id, *p, **kw):
        log = getlogger(__name__, self.__class__.__name__, 'edit')
        wp = model.WikiPage.query.get(_id=ObjectId(_id))
        log.debug('title: %s' % (wp.title))
        return {'page': wp}

    @expose()
    def save(self, pagetitle, text, _id):
        log = getlogger(__name__, self.__class__.__name__, 'save')
        wp = model.WikiPage.query.get(_id=ObjectId(_id))
        log.debug('title: %s' % (wp.title))
        wp.title = pagetitle
        wp.text = text
        redirect ('/%s' % urllib.quote(pagetitle))
    
    @expose('nessiewiki.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    @expose('nessiewiki.templates.login')
    def login(self, came_from=lurl('/')):
        """Start the user login."""
        login_counter = request.environ.get('repoze.who.logins', 0)
        if login_counter > 0:
            flash(_('Wrong credentials'), 'warning')
        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from)

    @expose()
    def post_login(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                params=dict(came_from=came_from, __logins=login_counter))
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)
        redirect(came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        redirect(came_from)
