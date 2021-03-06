# -*- coding: utf-8 -*-
"""复写tornado的请求基类"""

import json
import redis
# import torndb
import tornado
from .session import Session
import app.conf as config


class Application(tornado.web.Application):
    """定制的Application，用来补充db数据库实例"""

    def __init__(self, *args, **kwargs):
        # 调用执行父类tornado.web.Application的初始化方法
        super(Application, self).__init__(*args, **kwargs)

        # 构造数据库连接对象
        # self.db = torndb.Connection(**config.MYSQL_OPTIONS)

        # 构造redis连接实例
        self.redis = redis.StrictRedis(**config.REDIS_OPTIONS)


class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        """提供对数据库连接实例db的属性操作"""
        return self.application.db

    @property
    def redis(self):
        """提供对Redis连接实例redis的属性操作"""
        return self.application.redis

    def get_current_user(self):
        """
        判断用户登录是否成功
        :return: 登陆成功返回用户的昵称，否则返回None
        """
        # self.session = Session(self)
        user_json = self.get_secure_cookie('user')
        print(user_json, '--base : user_json'*2)
        if user_json:
            return tornado.escape.json_decode(user_json)
        else:
            return None

    # def get_user_locale(self):
    #     user_json = self.get_secure_cookie('user')
    #     print(user_json, '=+'*20)
    #     if user_json:
    #         return tornado.escape.json_decode(user_json)
    #     else:
    #         return None

    def prepare(self):
        if self.request.headers.get('Content-Type', '').startswith('application/json'):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = {}

    # def set_default_headers(self):
    #     """设置默认的响应报文中的header，默认返回json格式数据. 加上这个之后好像返回的数据有点固定"""
    #     self.set_header("Content-Type", "application/json; charset=UTF-8")

    # def data_received(self, chunk):
    #     """implement this method to handle streamed request data.

    #     requires the `.stream_request_body` decorator.
    #     """
    #     print('好像用不着这个方法', chunk)
    #     return chunk


class PageNotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        raise tornado.web.HTTPError(404)

tornado.web.ErrorHandler = PageNotFoundHandler
