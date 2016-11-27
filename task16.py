#! /usr/bin/env python2.7

from collections import Sequence, Iterator

class xrange_adhoc(Sequence, Iterator):

    def __init__(self, *args):
        if len(args) == 1:
            start, stop, step = 0, args[0], 1
        elif len(args) == 2:
            start, stop, step = args[0], args[1], 1
        elif len(args) == 3:
            start, stop, step = args
        else:
            raise TypeError('xrange_adhoc() requires 1-3 int arguments')

        try:
            start, stop, step = int(repr(start)), int(repr(stop)), int(repr(step))
        except ValueError:
            raise TypeError('an integer is required')


        if step == 0:
            raise ValueError('xrange_adhoc() arg 3 must not be zero')
        elif step < 0:
            stop = min(stop, start)
        else:
            stop = max(stop, start)

        self._start = start
        self._stop = stop
        self._step = step
        self._len = (stop - start) // step + bool((stop - start) % step)

        self._head = start - step # for iterating

    def __getitem__(self, index):
        if index < 0:
            index += self._len
        if index < 0 or index >= self._len:
            raise IndexError('xrange_adhoc index out of range')
        return self._start + index * self._step

    def __reversed__(self):
        sign = self._step / abs(self._step)
        last = self._start + ((self._len - 1) * self._step)
        return xrange_adhoc(last, self._start - sign, -1 * self._step)

    def __iter__(self):
        return self

    def next(self):
        if abs(self._stop - self._head) <= abs(self._step):
            raise StopIteration
        self._head += self._step
        return self._head

    def __len__(self):
        return self._len

    def __repr__(self):
        if self._start == 0 and self._step == 1:
            return 'xrange_adhoc(%d)' % self._stop
        elif self._step == 1:
            return 'xrange_adhoc(%d, %d)' % (self._start, self._stop)
        return 'xrange_adhoc(%d, %d, %d)' % (self._start, self._stop, self._step)

    def __str__(self):
        return self.__repr__();

print [i for i in xrange_adhoc(10)]
print [i for i in xrange(10)]
print [i for i in xrange_adhoc(1, 10)]
print [i for i in xrange(1, 10)]
print [i for i in xrange_adhoc(1, 10, 2)]
print [i for i in xrange(1, 10, 2)]
print [i for i in xrange_adhoc(10, 1, -2)]
print [i for i in xrange(10, 1, -2)]
print [i for i in xrange_adhoc(1, 10, -2)]
print [i for i in xrange(1, 10, -2)]
print [i for i in reversed(xrange_adhoc(10, 1, -2))]
print [i for i in reversed(xrange(10, 1, -2))]
print reduce(lambda x, y: x + y, xrange_adhoc(5))