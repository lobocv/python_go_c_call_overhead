from __future__ import print_function
import contextlib
import time
from ctypes import cdll




@contextlib.contextmanager
def time_print(task_name=""):
    t = time.time()
    try:
        yield
    finally:
        print(task_name, ":", time.time() - t, "s")



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


assert(cresult == goresult)

print('C time  = %f total \t%f per call' % (ctime, ctime / N_calls))
print('Go time = %f total\t%f per call' % (gotime, gotime / N_calls))
print("C = %.1f times faster" % (gotime / ctime))

