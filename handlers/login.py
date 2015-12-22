from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login/login.html")
