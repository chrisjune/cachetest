from unittest import mock
from django.test import modify_settings, override_settings
from fakeredis import FakeServer, FakeRedis
import django_redis
import os
from django.core.cache import caches, CacheHandler
from django.core import cache

server = {}


class CacheTest:
    def __init__(self, alias='default'):
        self.alias = alias
        # self.setting = modify_settings(
        #     CACHES={
        #         'append': {
        #             f'{alias}': {
        #                 'BACKEND': 'django_redis.cache.RedisCache',
        #                 'LOCATION': 'redis://127.0.0.1:6379/0',
        #                 "OPTIONS": {
        #                     "REDIS_CLIENT_CLASS": "fakeredis.FakeStrictRedis",
        #                 }
        #             }
        #         }
        #     }
        # )
        self.setting = override_settings(
            CACHES={
                f'{alias}': {
                    'BACKEND': 'django_redis.cache.RedisCache',
                    'LOCATION': 'redis://127.0.0.1:6379/0',
                    "OPTIONS": {
                        "REDIS_CLIENT_CLASS": "fakeredis.FakeStrictRedis",
                    }
                }
            }
        )

    def get_r(self):
        r_server = server.get(self.alias)
        if not r_server:
            r_server = FakeRedis(server=FakeServer())
            server[self.alias] = r_server
        return r_server

    def __call__(self, func):
        print('call')
        mock.patch.object(django_redis, 'get_redis_connection', return_value=self.get_r()).start()
        return self.setting(func)


    def __enter__(self):
        print('enter')
        return None

    def __exit__(self):
        print('exit')
