import redis
import time
import fakeredis

def is_redis_available(database):
    try:
        return database.ping()
    except (ConnectionRefusedError, redis.BusyLoadingError) as error:
        return False

def main():
    database = fakeredis.FakeRedis('redis')
    # Load data here
    while not is_redis_available(database):
        print("Busy Loading")
        time.sleep(30)
    # then Code in work generator accessing redis
        

if __name__=='__main__':
    main()
