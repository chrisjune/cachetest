SECRET_KEY = "test"
# # DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
CACHES = {
    # 'default': {
    #     'BACKEND': 'django_redis.cache.RedisCache',
    #     'LOCATION': 'redis://127.0.0.1:6379/10',
    #     'OPTIONS': {
    #         'CLIENT_CLASS': 'fakeredis.FakeStrictRedis',
    #     }
    # },
    # 'secondary': {
    #     'BACKEND': 'django_redis.cache.RedisCache',
    #     'LOCATION': 'redis://127.0.0.1:6379/1',
    #     'OPTIONS': {
    #         # 'CLIENT_CLASS': 'django_redis.client.DefaultClient',
    #         'CLIENT_CLASS': 'fakeredis.FakeStrictRedis',
    #     }
    # },
    # 'third': {
    #     "default": {
    #         "BACKEND": "django.core.cache.backends.dummy.DummyCache"
    #     }
    # }
}
