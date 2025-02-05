import json
from datetime import timedelta

from fastapi import HTTPException
import redis

def initialize_redis_client():
    try:
        client = redis.Redis(host="localhost", port=6379, db=0)
        client.ping()
        return client
    except redis.ConnectionError:
        raise Exception("Could not connect to Redis. Ensure Redis is running.")

def cache_in_redis(key: str, data: dict, expiration: timedelta = timedelta(days=1)):
    # Store the data in Redis (as a JSON string)
    redis_client = initialize_redis_client()
    redis_client.setex(key, expiration, json.dumps(data))

def get_from_redis(key: str) -> dict:
    cached_data = get_key(key)
    if cached_data:
        return json.loads(cached_data)
    return None


def set_key(key: str, value: str):
    redis_client = initialize_redis_client()
    response = redis_client.set(key, value)
    if response:
        return
    else:
        raise HTTPException(detail=f'Key-Value pair was not saved')

def get_key(key: str):
    redis_client = initialize_redis_client()
    value = redis_client.get(key)
    if value:
        return value

def delete_key(key: str):
    redis_client = initialize_redis_client()
    response = redis_client.delete(key)
    if response:
        return
    else:
        raise HTTPException(detail=f'Key was not deleted')