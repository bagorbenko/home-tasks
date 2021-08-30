cache = {1:1}
def collatz_count(n):
    if n not in cache:
        if n % 2 == 0:
            cache[n] = 1 + collatz_count(n / 2)
        else:
            cache[n] = 1 + collatz_count(3 * n + 1)
    return cache[n]

len = 0
i = 1
while i < 10000000:
    len = collatz_count(10000000)
    i += 1
print(i)