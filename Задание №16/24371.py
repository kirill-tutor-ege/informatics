from functools import *

@lru_cache(None)
def F(n):
    return G(n - 2)

@lru_cache(None)
def G(n):
    if n < 100:
        return n
    if n >= 100:
        return F(n - 3) + 1

for i in range(100, 5000):
    F(i)

print(F(5000))
