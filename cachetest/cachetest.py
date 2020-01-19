from unittest import mock
from django.test import modify_settings, override_settings
from fakeredis import FakeServer, FakeRedis
import django_redis
import os
from django.core.cache import caches
from django.core.cache import CacheHandler

server = FakeServer()


class CacheTest:
    def __init__(self, default='default'):
        self.default = default

    def get_r(self):
        return FakeRedis(host=self.default, server=server)

    def __call__(self, func):
        mock.patch.object(django_redis, 'get_redis_connection', return_value=self.get_r()).start()
        # mock.patch.object(CacheHandler, '__init__', return_value=self.get_r()).start()
        return func

    def __enter__(self):
        print('enter')
        return None

    def __exit__(self):
        print('exit')
