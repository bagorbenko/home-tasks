import timeit
from numba import njit, prange

start = timeit.default_timer()

@njit(fastmath = True)
def d1(n):
    return 0 if n == 1 else 1+d1(n//2 if n % 2 == 0 else n*3+1)


def d2(g):
    pa = []
    for k in prange(1,g):
        pa.append(d1(k))
    i = 0
    index = 0
    max_len = 0
    for elem in pa:
        i += 1
        if elem > max_len:
            max_len = elem
            index = i
    return (index)
stop1 = timeit.default_timer()
print(d2(10**7))
print('Time: ', stop1 - start)
stop2 = timeit.default_timer()
print('Time 2: ', stop2 - start)