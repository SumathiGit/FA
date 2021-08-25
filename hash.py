import redis



r = redis.StrictRedis(host='localhost', port= 6379, db =0)
# Add key value pairs to the Redis hash
#Key , Field , Value
r.hset("SumVid", "12am", "/home/sumathi/FastAPI/videos/video1.mp4")
r.hset("SumVid", "1am", "/home/sumathi/FastAPI/videos/video2.mp4")
r.hset("SumVid", "2am", "/home/sumathi/FastAPI/videos/video3.mp4")
r.hset("SumVid", "3am", "/home/sumathi/FastAPI/videos/video4.mp4")
r.hset("SumVid", "4am", "/home/sumathi/FastAPI/videos/video5.mp4")
r.hset("SumVid", "5am", "/home/sumathi/FastAPI/videos/video6.mp4")
r.hset("SumVid", "6am", "/home/sumathi/FastAPI/videos/video7.mp4")
r.hset("SumVid", "7am", "/home/sumathi/FastAPI/videos/video8.mp4")
r.hset("SumVid", "8am", "/home/sumathi/FastAPI/videos/video9.mp4")
r.hset("SumVid", "9am", "/home/sumathi/FastAPI/videos/video10.mp4")
r.hset("SumVid", "10am", "/home/sumathi/FastAPI/videos/video11.mp4")
r.hset("SumVid", "11am", "/home/sumathi/FastAPI/videos/video12.mp4")
r.hset("SumVid", "12pm", "/home/sumathi/FastAPI/videos/video13.mp4")
r.hset("SumVid", "1pm", "/home/sumathi/FastAPI/videos/video14.mp4")
r.hset("SumVid", "2pm", "/home/sumathi/FastAPI/videos/video15.mp4")
r.hset("SumVid", "3pm", "/home/sumathi/FastAPI/videos/video16.mp4")
r.hset("SumVid", "4pm", "/home/sumathi/FastAPI/videos/video17.mp4")
r.hset("SumVid", "5pm", "/home/sumathi/FastAPI/videos/video18.mp4")
r.hset("SumVid", "6pm", "/home/sumathi/FastAPI/videos/video19.mp4")
r.hset("SumVid", "7pm", "/home/sumathi/FastAPI/videos/video20.mp4")
r.hset("SumVid", "8pm", "/home/sumathi/FastAPI/videos/video21.mp4")
r.hset("SumVid", "9pm", "/home/sumathi/FastAPI/videos/video22.mp4")
r.hset("SumVid", "10pm", "/home/sumathi/FastAPI/videos/video23.mp4")
r.hset("SumVid", "11pm", "/home/sumathi/FastAPI/videos/video24.mp4")


r.save

 

# Retrieve the value for a specific key

getting_Video1 = r.hget("SumVid", "12am") #byte
getting_Video2 = r.hget("SumVid", "1am")
getting_Video3 = r.hget("SumVid", "2am")
getting_Video4 = r.hget("SumVid", "3am")
getting_Video5 = r.hget("SumVid", "4am")
getting_Video6 = r.hget("SumVid", "5am")
getting_Video7 = r.hget("SumVid", "6am")
getting_Video8 = r.hget("SumVid", "7am")
getting_Video9 = r.hget("SumVid", "8am")

#Need to decode every single video
decoding_vid = getting_Video1.decode('utf-8', 'ignore') #\
print(decoding_vid)
print(type(decoding_vid)) #string


print("Value for the key 3 is")

print(r.hget("SumVid", "2am"))

 

print("The keys present in the Redis hash:")

print(r.hkeys("SumVid"))

 

print("The values present in the Redis hash:")

print(r.hvals("SumVid"))

 

print("The keys and values present in the Redis hash are:")

print(r.hgetall("SumVid"))