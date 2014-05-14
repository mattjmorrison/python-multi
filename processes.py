from multiprocessing import Process, Pool
import timeit

def doit(item):
    print "Doing it with {}".format(item)


def start():
    pool = Pool(processes=2)
    for item in range(10):
        print "Sending {}".format(item)
        pool.apply_async(doit, [item])
    pool.close()
    pool.join()
    print "Done"


def main():
    print timeit.Timer(start).timeit()
