import threading
import time

shared_variable = 0
lock = threading.Lock()

def increment():
    global shared_variable
    for _ in range(1000000):
        lock.acquire()
        try:
            global shared_variable
            shared_variable += 1
        finally:
            lock.release()

def decrement():
    global shared_variable
    for _ in range(1000000):
        lock.acquire()
        try:
            global shared_variable
            shared_variable -= 1
        finally:
            lock.release()

def main():
    print(f"Initial value: {shared_variable}")
    
   
    thread1 = threading.Thread(target=increment)
    thread2 = threading.Thread(target=decrement)

    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print(f"Final value: {shared_variable}")

if __name__ == "__main__":
    main()