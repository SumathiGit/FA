from fastapi import FastAPI, applications
from uvicorn import run
from fastapi import FastAPI, Request, Response
from connection import redis_cache

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


@app.get("/")
def read_root():
    return {"Redis": "FastAPI"}

#root > Get all keys from the redis DB
@app.get('/RedisKeys')
async def redis_keys():
    return await get_all()

#we can set a value for a key 
@app.get('/Firstpage')
async def set(key, value):
        return await redis_cache.set(key, value)

#we can get the value for a particular key
@app.get('/Secondpage')
async def get(key):
        return await redis_cache.get(key)



#we can create a hash 
@app.get("/createhash")
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























if __name__ == '__main__':
    run("main:app", port=3000, reload=True)