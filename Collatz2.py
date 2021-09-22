import timeit
from numba import prange
start = timeit.default_timer()
cache = {1: 1}
def d1(n):
    if n not in cache:
        if n % 2 == 0:
            cache[n] = 1 + d1(n / 2)
        else:
            cache[n] = 1 + d1(3 * n + 1)
    return cache[n]

def d2(g):
    a = []
    for n in prange(1, g):
        a.append(d1(n))
    i = 0
    index = 0
    max_len = 0
    for e in a:
        i += 1
        if e > max_len:
            max_len = e
            index = i
    return(index)
print(d2(10**6))
stop = timeit.default_timer()
print('Time: ', stop - start)