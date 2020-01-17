SECRET_KEY = "test"
# DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
CACHES = {
    "default": {
        'BACKEND': 'django_redis.cache.RedisCache',
        'OPTIONS': {
            'CLIENT_CLASS': 'fakeredis.FakeRedis',
        }
    }
}