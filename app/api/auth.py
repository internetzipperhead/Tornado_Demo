# -*- coding: utf-8 -*-
"""权限认证"""

from app.util.base import BaseHandler


class RegisterHandler(BaseHandler):

    def post(self):
        pass


class LoginHandler(BaseHandler):

    def post(self):
        items = ['item1', 'item2', 'item3']
        self.write(items)


class LogoutHandler(BaseHandler):

    def post(self):
        pass


class ImageCodeHandler(BaseHandler):

    def get(self):
        pass


class SMSCodeHandler(BaseHandler):

    def get(self):
        pass
