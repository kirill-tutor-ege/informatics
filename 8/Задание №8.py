# Быстро получить алфавит системы счисления с основанием n
from string import *

(digits + ascii_uppercase)[:n]

word = "" 
 
# Проверить, чтобы символ под номером n был равен m 
if word[n - 1] == "m": pass 
# Пример: проверить, чтобы 2-ая буква была буквой Я 
if word[1] == "Я": pass 
 
# Посчитать, сколько раз встречается символ m 
word.count("m") 
# Пример: Проверить, чтобы было ровно 2 буквы А 
if word.count("А") == 2: pass 

# Проверить, чтобы все символы были различны 
if (len(set(word)) == len(word)): pass 
 
# Проверить, чтобы все символы (кроме одного) были различны 
if (len(set(word)) == len(word) - 1): pass 

# Проверить, чтобы все символы, принадлежащие одной категории(n1, n2, n3), встречались ровно n раз 
if (word.count("n1") + word.count("n2") + word.count("n3") == n): pass 
# Пример: Слова составляют из букв ЗИМА, нам подходят только слова, в которых 1 гласная 
if word.count("А") + word.count("И") == 1: pass
# Пример с генератором
if sum([word.count(x) for x in "ИА"]) == 1: pass

# Проверить, чтобы символ под индексом i принадлежал одной категории(n1, n2, n3), встречались ровно n раз 
if word[i] in "n1n2n3": pass 
# Проверить, что слово начинается с гласной
if word[0] in "АЕУОИЯЮ": pass
 
# Проверить, чтобы в слове не встречалось последовальности символов ABC 
if "ABC" not in word: pass 
# Пример: Проверить, чтобы символы А и Б не стояли рядом 
if "АБ" not in word and "БА" not in word: pass 
 
# никакие две чётные и две нечётные цифры не стоят рядом 
# заменяем все нечетные на единицу, а все четные на 0 
# Пример: 
temp = word.replace("7", "1").replace("5", "1").replace("3", "1")\
            .replace("6", "0").replace("4", "0").replace("2", "0") 
if ("00" not in temp) and ("11" not in temp): pass

temp = "".join(str(int(x) % 2) for x in word)
if ("00" not in temp) and ("11" not in temp): pass 

# Сложный пример с генератором
(all("".join(x) not in word for x in product("02468", repeat=2))) and (all("".join(x) not in word for x in product("13579", repeat=2)))

# Посчитать, каким слово встречается по счету 
number = 0 
for i in product(...) ИЛИ permutations(...): # В зависимости от задания 
    word = "".join(i) 
    number += 1
    if наше условие: 
        print(number) 

# Посчитать количество слов, удовлетворяющих условию 
count = 0 
for i in product(...) ИЛИ permutations(...): # В зависимости от задания 
    word = "".join(i) 
    if наше условие: 
        count += 1 
print(count)