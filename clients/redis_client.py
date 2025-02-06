import json
from datetime import timedelta
from fastapi import HTTPException
import redis

# Initialize Redis client once to avoid repeated connections
def get_redis_client():
    try:
        client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
        client.ping()
        return client
    except redis.ConnectionError:
        raise Exception("Could not connect to Redis. Ensure Redis is running.")

redis_client = get_redis_client()

def cache_in_redis(key: str, data: dict, expiration: timedelta = timedelta(days=1)):
    """Caches data in Redis with an expiration time."""
    try:
        redis_client.setex(key, expiration.total_seconds(), json.dumps(data))
    except redis.RedisError as e:
        raise HTTPException(status_code=500, detail=f"Redis caching error: {str(e)}")

def get_from_redis(key: str) -> dict | None:
    """Retrieves data from Redis and returns it as a dictionary."""
    cached_data = redis_client.get(key)
    return json.loads(cached_data) if cached_data else None

def set_key(key: str, value: str):
    """Sets a key-value pair in Redis."""
    try:
        if not redis_client.set(key, value):
            raise HTTPException(status_code=500, detail="Failed to set key in Redis")
    except redis.RedisError as e:
        raise HTTPException(status_code=500, detail=f"Redis set key error: {str(e)}")

def get_key(key: str) -> str | None:
    """Gets a value from Redis by key."""
    return redis_client.get(key)

def delete_key(key: str):
    """Deletes a key from Redis."""
    try:
        if redis_client.delete(key) == 0:
            raise HTTPException(status_code=404, detail="Key not found in Redis")
    except redis.RedisError as e:
        raise HTTPException(status_code=500, detail=f"Redis delete key error: {str(e)}")
