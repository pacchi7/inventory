from django.conf import settings
from datetime import timedelta
from .utils import get_redis_connection
import redis


import json

def set(key, value, expire_time=None):
    try:

        r = get_redis_connection()
        if isinstance(value, dict):  # Check if the value is a dict
            value = json.dumps(value)  # Convert dict to JSON string
        value  = json.dumps(value)
        if expire_time is not None:
            expiration_time = timedelta(minutes=int(expire_time))
            redis_out = r.setex(key, expiration_time, value)
        else:
            redis_out = r.set(key, value)
        return redis_out
    except redis.RedisError as e:
        print(f"Redis error: {e}")
        return e
    except Exception as e:
        print(f"An error occurred: {e}")
        return e
def get(key):
    try:
        r = get_redis_connection()
        value = r.get(key)
        if value:
            return json.loads(value)  # Convert JSON string back to dict
        else:
            return None
    except redis.RedisError as e:
        print(f"Redis error: {e}")
        return e
    except Exception as e:
        print(f"An error occurred: {e}")
        return e


def string_value_get(key):
    try:
        r = get_redis_connection()
        value = r.get(key)
        value = value.decode('utf-8')
        return value

    except redis.RedisError as e:
        return e
    except Exception as e:
        return e


def delete(key):
    try:
        r = get_redis_connection()
        deleted_count = r.delete(key)
        return deleted_count
    except redis.RedisError as e:
        return 0
    except Exception as e:
        return e
