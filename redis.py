import json
from fastapi import HTTPException
import redis


def redis_instance():
    return redis.Redis(host="localhost", port=6379, db=0)


def set_key(key: str, value: str):
    redis_client = redis_instance()
    response = redis_client.set(key, value)
    if response:
        return
    else:
        raise HTTPException(detail=f'Key-Value pair was not saved')


def get_key(key: str):
    redis_client = redis_instance()
    value = redis_client.get(key)
    if value:
        return value
    else:
        raise HTTPException(detail=f'Key was not found')



def delete_key(key: str):
    redis_client = redis_instance()
    response = redis_client.delete(key)
    if response:
        return
    else:
        raise HTTPException(detail=f'Key was not deleted')