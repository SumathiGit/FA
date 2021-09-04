**Creating a API using FastAPI with REDIS Database**


step1:
>hash.py >> Create hashes using hset and add them into redis db

step2:
>Add all the hashes into single set using sadd

step3:
>connection.py >> made a connection with Redis db using redis_cache

step4:
>main.py >> Access db with GET,SET,and POST methods

step5:
>To run API : uvicorn main:app --reload



**RedisServer and Redis-cli**

Step1:
>To start redis server on
>Terminal : **redis-server**

>To stop  : **sudo service redis-server stop**

>To start redis client on
>Terminal : **redis-cli**

>Type keys* to get all the keys from the db
