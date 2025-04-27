import threading
import time

shared_variable = 0
mutex = threading.Lock()

def increment():
    global shared_variable
    for _ in range(1000000):
        mutex.acquire()
        global shared_variable
        shared_variable += 1
        mutex.release()
        time.sleep(0.0001)

def decrement():
    global shared_variable
    for _ in range(1000000):
        mutex.acquire()
        global shared_variable
        shared_variable -= 1
        mutex.release()
        time.sleep(0.0001)

print(f"Initial value: {shared_variable}")

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Final value: {shared_variable}")