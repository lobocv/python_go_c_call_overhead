from __future__ import print_function
import contextlib
import time
import pyfunc
from ctypes import cdll


golib = cdll.LoadLibrary('./gofunc.so')
print("Loaded go generated SO library")

N_calls = 1000000

print ('Starting test with N_calls = %d' % N_calls)

t0 = time.time()
for i in xrange(N_calls):
    goresult = golib.add(2, 3)
t1 = time.time()

gotime = t1 - t0


clib = cdll.LoadLibrary('./cfunc.so')
print("Loaded C generated SO library")
t0 = time.time()
for i in xrange(N_calls):
    cresult = clib.add(2, 3)
t1 = time.time()

ctime = t1 - t0


t0 = time.time()
for i in xrange(N_calls):
    pyresult = pyfunc.add(2, 3)
t1 = time.time()

pytime = t1 - t0


assert(cresult == goresult)
assert(cresult == pyresult)

print('C      time = %f seconds total\t%f per call' % (ctime, ctime / N_calls))
print('Go     time = %f seconds total\t%f per call' % (gotime, gotime / N_calls))
print('Python time = %f seconds total\t%f per call' % (pytime, pytime / N_calls))

print("C = %.1f times faster than Go" % (gotime / ctime))
print("C = %.1f times faster than Python" % (pytime / ctime))

