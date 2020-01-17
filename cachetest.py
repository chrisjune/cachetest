from unittest import mock
from django.test import modify_settings
from fakeredis import FakeServer, FakeRedis
import django_redis
import os

server = FakeServer()


class CacheTest:
    def __init__(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
        self.setting = modify_settings(
            CACHES={
                "default": {
                    'BACKEND': 'django_redis.cache.RedisCache',
                    'OPTIONS': {
                        'CLIENT_CLASS': 'fakeredis.FakeRedis',
                    }
                }
            }
        )

        os.environ.get('DJANGO_SETTINGS_MODULE')

    def get_r(self):
        return FakeRedis(server=server)

    def __call__(self, func):
        print('call')
        mock.patch.object(django_redis, 'get_redis_connection', return_value=self.get_r()).start()
        return func

    def __enter__(self):
        print('enter')
        return None

    def __exit__(self):
        print('exit')


@CacheTest()
def test_a():
    print('a')
    conn = django_redis.get_redis_connection()
    conn.set('a','b')
    print(conn)


if __name__ == '__main__':
    test_a()
    conn = django_redis.get_redis_connection()
    assert conn.get('a') == b'b'
