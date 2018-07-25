from queue import Queue
from threading import Thread
import time

# A thread that produces data
def producer(out_q):
    for i in range(10):
        # Produce some data
        data = i
        out_q.put(data)
        time.sleep(1)

# A thread that consumes data
def consumer(in_q):
    while True:
# Get some data
        data = in_q.get()
        print(data)
        time.sleep(1)

# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()