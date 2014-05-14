from threading import Thread
from Queue import Queue
import timeit

queue = Queue()
def doit():
    while True:
        item = queue.get()
        print "Working on {}".format(item)
        queue.task_done()

def start_threads(count):
    for thing in range(count):
        t = Thread(target=doit)
        t.daemon = True
        t.start()

def main():
    start_threads(10)
    for item in range(1, 10000):
        queue.put(item)
    queue.join()
    print "Done!"

if __name__ == '__main__':
    print timeit.Timer(main).timeit(number=1)
