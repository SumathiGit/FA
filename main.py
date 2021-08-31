from fastapi import FastAPI, applications
from uvicorn import run
from fastapi import FastAPI, Request, Response
from connection import redis_cache
from hash import r


app = FastAPI(title="FastAPI with Redis")


async def get_all():
    return await redis_cache.keys('*')


@app.on_event('startup')
async def starup_event():
    await redis_cache.init_cache()


@app.on_event('shutdown')
async def shutdown_event():
    redis_cache.close()
    await redis_cache.wait_closed()

#root
@app.get("/")
def read_root():
    return {"Redis": "FastAPI"}

#root > Get all keys from the redis DB
@app.get('/RedisKeys')
async def redis_keys():
    return await get_all()

#we can set a value for a key 
@app.post('/create_keyValue')
async def set(key, value):
        return await redis_cache.set(key, value)

#we can get the value for a particular key
@app.get('/GetValue4Key')
async def get(key):
        return await redis_cache.hvals(key)



#we can create a hash 
@app.post("/createhash")
async def hset(key, field, value):
        return await redis_cache.hset(key,field, value)



#we can get the values for a particular hash key with their respective field
@app.get("/hgetall_hash")
async def get(key):
        return await redis_cache.hgetall(key)


#get only values from a particular hash
@app.get("/hvals_hash")
async def get(key):
        return await redis_cache.hvals(key)


#hash >> get value using Field name
@app.get("/get_particular_hashvalue")
async def get(key, field):
        return await redis_cache.hget(key, field)


#optional
@app.get("/sets_of_hash") 
async def smembers(key):
        result =redis_cache.smembers(key)
        return await result


@app.get("/lastweek")
def sort():
        lastweeklist = r.sort("date", 24, 31, alpha=True) #sorted set key > date
        pipe = r.pipeline()
        for keys in lastweeklist:
                pipe.hgetall(keys)
        week1 = []
        for week in pipe.execute():
                week1.append(week)
        return week1




if __name__ == '__main__':
    run("main:app", port=3000, reload=True)
