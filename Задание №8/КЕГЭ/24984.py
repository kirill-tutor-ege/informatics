from itertools import *
from string import *

count = 0
for i in product((digits + ascii_uppercase)[:16], repeat = 5):
    word = "".join(i)
    if  (word[0] != '0') and \
        any(x in word for x in "149") and\
        all(word.count(x) <= 2 for x in (digits + ascii_uppercase)[:16]):
        count += 1
print(count)
