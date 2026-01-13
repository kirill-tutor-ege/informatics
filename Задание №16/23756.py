from functools import *

@lru_cache(None)
def G(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return G(n - 2) + 1

def F(n):
    return 2 * (G(n - 3) + 8)

for x in range(1, 15548):
    G(x)

print(F(15548))
