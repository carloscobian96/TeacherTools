import http
import threading
from urllib import request
import json

from setuptools import Require
addressURL = "http://192.168.0.101/protoapi/user"

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
    def run(self):
        while (True):
            req = request.Request(addressURL)  
            print(f"{json.loads(req)} {self.threadID} success") 


    

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-2", 3)
thread4 = myThread(4, "Thread-2", 4)
thread5 = myThread(5, "Thread-2", 5)


# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

print("started")

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)
threads.append(thread5)


