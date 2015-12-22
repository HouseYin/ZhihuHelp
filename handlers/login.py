from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login/login.html")

    def post(self):
        account = self.get_argument('account')
        password = self.get_argument('password')
        captcha = self.get_argument('captcha',default=None)
        return
