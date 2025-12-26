from itertools import *
from string import *

def check(number):
    count = 0
    for i in range(len(number) - 1):
        if number[i] in "13579B" and number[i + 1] in "13579B":
            count += 1
    return count <= 2

count = 0
for i in product((digits + ascii_uppercase)[:12], repeat = 5):
    word = "".join(i)
    if (word[0] != '0') and check(word):
        count += 1
print(count)
