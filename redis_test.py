import redis
import time
import fakeredis

def is_redis_available():
    try:
        # return fakeredis.FakeRedis('localhost').ping() # Not sure if the database is at localhost or 'redis'
        return redis.Redis('redis').ping() # Not sure if the database is at localhost or 'redis'
    except (ConnectionRefusedError, redis.BusyLoadingError) as error:
        print(error)
        return False

def main():
    if is_redis_available():
        database = redis.Redis('redis')
        # database = fakeredis.FakeRedis('redis')
    else:
        # Wait for redis to start
        time.sleep(30)

if __name__=='__main__':
    main()
