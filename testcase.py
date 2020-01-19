import django_redis
from cachetest.cachetest import CacheTest
import unittest
from django.core.cache import cache, caches
import os
import redis

class TestCase(unittest.TestCase):
    @CacheTest()
    def test_a(self):
        conn = django_redis.get_redis_connection()
        conn.set('a','b')

    @CacheTest()
    def test_b(self):
        conn = django_redis.get_redis_connection()
        assert conn.get('a') == b'b'

    # @CacheTest('redis')
    # def test_c(self):
    #     conn = caches['redis']
    #     conn.set('c', 'd', 10)
    #     conn.get('c') == b'd'

    # @CacheTest('redis')
    # def test_d(self):
    #     conn = caches['redis']
    #     conn.get('c') == b'd'
    #
    # @CacheTest('redis')
    # def test_e(self):
    #     conn = django_redis.get_redis_connection('redis')
    #     conn.get('c') == b'd'

if __name__ == '__main__':
    unittest.main()
