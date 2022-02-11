import redis
import time
import fakeredis

def is_redis_available():
    try:
        # return fakeredis.FakeRedis('localhost').ping() # Not sure if the database is at localhost
        return redis.Redis('localhost').ping() # Not sure if the database is at localhost
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