# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# - символ «?» означает ровно одну произвольную цифру;
# - символ «*» означает любую последовательность произвольной длины; в том числе «*» может задавать и пустую последовательность.

# Например, маске 123*4?5 соответствуют числа 123405 и 12300405.
# Среди натуральных чисел, не превышающих 10**10, найдите все числа, соответствующие маске 4*4736*1, которые делятся на 7993 без остатка. 
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце - соответствующие им результаты деления этих чисел на 7993.
# Количество строк в таблице для ответа избыточно.

# Сначала перебираем кратные, а потом проверяем на соотвествие маске
from fnmatch import fnmatch

for n in range(0, 10**10 + 1, 7993):
    if fnmatch(str(n), "4*4736*1"):
        print(n, n / 7993)


# Сначала перебираем соответствующие маске а потом проверяем на кратность
# 10000000000
# 4*4736***1 → на 2 звездочки не более 4-х цифр
from itertools import *

masked = [] 
for both_len in range(4 + 1): # n - суммарная длина двух "*"
    for star1_len in range(0, both_len + 1):
        star2_len = both_len - star1_len
        print(star1_len, star2_len)

        for star1 in product("0123456789", repeat = star1_len):
            star1 = "".join(star1)
            for star2 in product("0123456789", repeat = star2_len):
                star2 = "".join(star2)
                masked.append(int(f"4{star1}4736{star2}1"))
masked.sort()

for x in masked:
    if x % 7993 == 0:
        print(x, x / 7993)

# Если была бы маска с "?" → 4?4736*1
# 10000000000
# 4?4736***1 → не более 3-х цифр
from itertools import *

masked = []
for q in "0123456789":
    for n in range(3 + 1):
        for star in product("0123456789", repeat = n):
            star = "".join(star)
            masked.append(int(f"4{q}4736{star}1"))
masked.sort()

for x in masked:
    if x % 7993 == 0:
        print(x, x / 7993)

#~~~~~~~~~~~~~~~~~~~~~~~~~
# Делители
#~~~~~~~~~~~~~~~~~~~~~~~~~
def getDivs(n):
    divs = set()
    q = int(n ** 0.5)
    for div in range(1, q + 1):
        if n % div == 0:
            divs.add(div)
            divs.add(n // div)
    divs = sorted(divs)
    return divs

def isSimple(n):
    q = int(n ** 0.5)
    for i in range(2, q + 1):
        if n % i == 0:
            return False
    return True

# Пусть R – сумма всех различных натуральных делителей целого числа.
# Напишите программу, которая перебирает целые числа, бо́льшие 500 000, в порядке возрастания и ищет среди них такие, для которых
# значение R оканчивается на цифру 6. В ответе запишите в первом столбце таблицы первые пять найденных чисел в порядке возрастания, 
# а во втором столбце – пять соответствующих этим числам значений R.
# Например, для числа 20 R = 1 + 2 + 4 + 5 + 10 + 20 = 42.
# Количество строк в таблице для ответа избыточно. 
def getDivs(n):
    divs = set()
    q = int(n ** 0.5)
    for div in range(1, q + 1):
        if n % div == 0:
            divs.add(div)
            divs.add(n // div)
    divs = sorted(list(divs))
    return divs

for x in range(500_001, 501_000):
    divs = getDivs(x)
    R = sum(divs)
    if abs(R) % 10 == 6:
        print(x, R)

# Вывести только первые 5 чисел
count = 0
for x in range(500_001, 501_000):
    divs = getDivs(x)
    R = sum(divs)
    if abs(R) % 10 == 6:
        print(x, R)
        count += 1
        if count == 5:
            break
        

# Обозначим через M сумму максимального и минимального числа среди простых делителей целого числа, не считая самого числа. 
# Если таких делителей у числа нет, то считаем значение M равным нулю. Напишите программу, которая перебирает целые числа, 
# большие 23 600 000, в порядке возрастания и ищет среди них такие, для которых значение M при делении на 213 даёт в остатке 171.
# Выведите первые 6 найденных чисел в порядке возрастания, справа от каждого числа запишите соответствующее значения M.  
# Количество строк для записи ответа избыточно.
def getDivs(n):
    divs = set()
    q = int(n ** 0.5)
    for div in range(2, q + 1):
        if n % div == 0:
            divs.add(div)
            divs.add(n // div)
    divs = sorted(list(divs))
    return divs

def isSimple(n):
    q = int(n ** 0.5)
    for i in range(2, q + 1):
        if n % i == 0:
            return False
    return True

for x in range(23_600_001, 23_700_000):
    divs = getDivs(x)
    simple_divs = []
    for div in divs:
        if isSimple(div):
            simple_divs.append(div)

    if len(simple_divs) > 0:
        M = min(simple_divs) + max(simple_divs)
    else:
        M = 0

    if M % 213 == 171:
        print(x, M)

for x in range(23_600_001, 23_700_000):
    divs = getDivs(x)
    simple_divs = [n for n in divs if isSimple(n)]

    M = 0
    if len(simple_divs) > 0:
        M = min(simple_divs) + max(simple_divs)

    if M % 213 == 171:
        print(x, M)
