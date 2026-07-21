'''
thread is concept that are os level sub process(shares same process) shares same memory

helps in running multiple tasks concurrently

-it is useful when a program spend a lot time waiting and 
    Reading/writing files
    Network requests (API calls)
    Database queries
    User input

=> todays world Asyncio taken up a lot of work in this i/o works(A single thread runs many tasks cooperatively)

'''

'''
every python programm starts with a main thread

'''

import threading,time

print(threading.current_thread().name)

def hello_db():
    time.sleep(10)
    print(threading.current_thread().name)


t1=threading.Thread(target=hello_db)

t1.start()
t1.join()  #forces to behave like without threads
# hello_db()

print(threading.current_thread().name)


# /////////////////////////////////////////


counter = 0
lock = threading.Lock()
def safe_increment():
    global counter
    for _ in range(100_000):
     with lock: # acquire -> critical section -> release (even on exception)
         counter += 1

threads = [threading.Thread(target=safe_increment) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)