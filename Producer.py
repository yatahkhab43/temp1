import threading
import queue
import time
import random

class ProducerConsumer:
    def __init__(self, buffer_size):
        self.buffer = queue.Queue(buffer_size)
        self.buffer_size = buffer_size

    def producer(self, items):
        for i in range(items):
            item = random.randint(1, 100)
            time.sleep(random.random())
            self.buffer.put(item)
            print(f"Produced: {item} | Buffer Size: {self.buffer.qsize()}")

    def consumer(self, items):
        for i in range(items):
            item = self.buffer.get()
            time.sleep(random.random())
            print(f"Consumed: {item} | Buffer Size: {self.buffer.qsize()}")
            self.buffer.task_done()

def main():
    BUFFER_SIZE = 5
    NUM_ITEMS = 10
    
    pc = ProducerConsumer(BUFFER_SIZE)

    producer_thread = threading.Thread(target=pc.producer, args=(NUM_ITEMS,))
    consumer_thread = threading.Thread(target=pc.consumer, args=(NUM_ITEMS,))

    print(f"Starting Producer-Consumer Simulation")
    print(f"Buffer Size: {BUFFER_SIZE}")
    print(f"Items to Produce/Consume: {NUM_ITEMS}\n")

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print("\nSimulation Complete")

if __name__ == "__main__":
    main()