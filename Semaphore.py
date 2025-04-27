import threading
import time
from threading import Semaphore

class ProcessSync:
    def __init__(self):
        self.shared_variable = 0
        self.semaphore = Semaphore(1)
        self.increment_count = 100000
        self.decrement_count = 100000

    def increment_thread(self):
        for _ in range(self.increment_count):
            self.semaphore.acquire()
            self.shared_variable += 1
            print(f"Increment: {self.shared_variable}")
            self.semaphore.release()
            time.sleep(0.0001)

    def decrement_thread(self):
        for _ in range(self.decrement_count):
            self.semaphore.acquire()
            self.shared_variable -= 1
            print(f"Decrement: {self.shared_variable}")
            self.semaphore.release()
            time.sleep(0.0001)

    def run(self):
        print(f"Initial value: {self.shared_variable}")

        t1 = threading.Thread(target=self.increment_thread)
        t2 = threading.Thread(target=self.decrement_thread)

        start_time = time.time()

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        end_time = time.time()

        print(f"\nFinal value: {self.shared_variable}")
        print(f"Total execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    process = ProcessSync()
    process.run()