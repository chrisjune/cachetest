import django_redis
from cachetest.cachetest import CacheTest
import unittest
from django.core.cache import caches


class TestCase(unittest.TestCase):

    @CacheTest()
    def test_mock_get_reids_connection(self):
        conn = django_redis.get_redis_connection()
        assert conn.set('alias', 'default')

    @CacheTest()
    def test_mock_get_reids_connection__check_same_server(self):
        conn = django_redis.get_redis_connection()
        assert conn.get('alias') == b'default'

    @CacheTest(alias='secondary')
    def test_mock_get_reids_connection__alias(self):
        conn = django_redis.get_redis_connection(alias='secondary')
        assert conn.set('alias', 'secondary')

    @CacheTest(alias='secondary')
    def test_mock_get_reids_connection__check_same_server__alias(self):
        conn = django_redis.get_redis_connection(alias='secondary')
        assert conn.get('alias') == b'secondary'

    @CacheTest()
    def test_mock_django_caches(self):
        conn = caches['default']
        conn.set('alias', 'default')
        assert conn.get('alias') == b'default'

    @CacheTest()
    def test_mock_django_caches__check_same_server(self):
        conn = caches['default']
        assert conn.get('alias') == b'default'

    @CacheTest(alias='secondary')
    def test_mock_django_caches__alias(self):
        conn = caches['secondary']
        conn.set('alias', 'secondary')
        assert conn.get('alias') == b'secondary'

    @CacheTest(alias='secondary')
    def test_mock_django_caches__check_same_server__alias(self):
        conn = caches['secondary']
        assert conn.get('alias') == b'secondary'

if __name__ == '__main__':
    unittest.main()
