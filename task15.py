#! /usr/bin/env python2.7

import time
from contextlib import contextmanager

class Timer(object):
    def __enter__(self):
    	self.start = time.time()
    def __exit__(self, type, value, traceback):
        print "Time elapsed: %g sec." % (time.time() - self.start)

@contextmanager
def timeit():
    start = time.time()
    yield None
    print "Time elapsed: %g sec." % (time.time() - start)

with Timer():
	time.sleep(1)

with timeit():
	time.sleep(2)