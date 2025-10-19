from re import *

line = open("24_21161.txt").readline()

non_zero_number = r"([1-9]\d*)"
number  = fr"({non_zero_number}|0)"
operator = r"([+-\/*])"
zero_operator = r"([+-*])"
pattern = fr"({number}(({operator}{non_zero_number})|({zero_operator}0)))"

# Вариант 1. Развернутый
max_len = 0
for x in finditer(pattern, line):
    substring = x.group(0)
    if len(substring) > max_len:
        max_len = len(substring)
print(max_len)

# Вариант 2. Генератор
print(max(len(x.group(0)) for x in finditer(pattern, line)))
