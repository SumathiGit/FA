import redis



r = redis.StrictRedis(host='localhost', port= 6379, db =0)
# Add key value pairs to the Redis hash
# Key , Field , Value
r.hset("26/8/21", "12am", "/home/sumathi/FastAPI/videos/video1.mp4")
r.hset("26/8/21", "1am", "/home/sumathi/FastAPI/videos/video2.mp4")
r.hset("26/8/21", "2am", "/home/sumathi/FastAPI/videos/video3.mp4")
r.hset("26/8/21", "3am", "/home/sumathi/FastAPI/videos/video4.mp4")
r.hset("26/8/21", "4am", "/home/sumathi/FastAPI/videos/video5.mp4")
r.hset("26/8/21", "5am", "/home/sumathi/FastAPI/videos/video6.mp4")
r.hset("26/8/21", "6am", "/home/sumathi/FastAPI/videos/video7.mp4")
r.hset("26/8/21", "7am", "/home/sumathi/FastAPI/videos/video8.mp4")
r.hset("26/8/21", "8am", "/home/sumathi/FastAPI/videos/video9.mp4")
r.hset("26/8/21", "9am", "/home/sumathi/FastAPI/videos/video10.mp4")
r.hset("26/8/21", "10am", "/home/sumathi/FastAPI/videos/video11.mp4")
r.hset("26/8/21", "11am", "/home/sumathi/FastAPI/videos/video12.mp4")
r.hset("26/8/21", "12pm", "/home/sumathi/FastAPI/videos/video13.mp4")
r.hset("26/8/21", "1pm", "/home/sumathi/FastAPI/videos/video14.mp4")
r.hset("26/8/21", "2pm", "/home/sumathi/FastAPI/videos/video15.mp4")
r.hset("26/8/21", "3pm", "/home/sumathi/FastAPI/videos/video16.mp4")
r.hset("26/8/21", "4pm", "/home/sumathi/FastAPI/videos/video17.mp4")
r.hset("26/8/21", "5pm", "/home/sumathi/FastAPI/videos/video18.mp4")
r.hset("26/8/21", "6pm", "/home/sumathi/FastAPI/videos/video19.mp4")
r.hset("26/8/21", "7pm", "/home/sumathi/FastAPI/videos/video20.mp4")
r.hset("26/8/21", "8pm", "/home/sumathi/FastAPI/videos/video21.mp4")
r.hset("26/8/21", "9pm", "/home/sumathi/FastAPI/videos/video22.mp4")
r.hset("26/8/21", "10pm", "/home/sumathi/FastAPI/videos/video23.mp4")
r.hset("26/8/21", "11pm", "/home/sumathi/FastAPI/videos/video24.mp4")


r.save

 

# Retrieve the value for a specific key

getting_Video1 = r.hget("26/8/21", "12am") #byte


#Need to decode every single video
decoding_vid = getting_Video1.decode('utf-8', 'ignore') #\
print(decoding_vid)
print(type(decoding_vid)) #string


print("Value for the key 3 is")
print(r.hget("26/8/21", "2am"))

 

print("The keys present in the Redis hash:")
print(r.hkeys("26/8/21"))

 

print("The values present in the Redis hash:")
print(r.hvals("26/8/21"))

 

print("The keys and values present in the Redis hash are:")
print(r.hgetall("26/8/21"))


# pipe = r.pipeline()
# for key in sorted(r.scan_iter()):
#     print(key)
#     pipe.hvals(key) #or hgetall(key)

# for h in pipe.execute():
#     print(h)
