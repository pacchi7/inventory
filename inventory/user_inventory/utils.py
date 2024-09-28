import string
import random
import redis
from django.conf import settings


def get_redis_connection():
    return redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
    
#     return password