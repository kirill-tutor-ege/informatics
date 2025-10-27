# 1. Типы данных
5, 1, 9, 3324   # int   — целые числа
5.0, 1.3        # float — вещественные числа
True, False     # bool  — логические значения
"abcde", '123'  # str   — строки

# X — данные, которые надо перевести из одного типа в другой
# Если надо перевести в целое число         -> int(X)
# Если надо перевести в вещественное число  -> float(X)
# Если надо перевести в логическое значение -> bool(X)
# Если надо перевести в строку              -> str(X)

# 2. Приведение типов
# 2.1 Целые числа
int(7.123) -> 7
int(7.999) -> 7
int("523") -> 523
int("abc") -> Ошибка
int(True)  -> 1
int(False) -> 0

# 2.2 Вещественные числа
float(7)        -> 7.0
float("523")    -> 523.0
float("12.5")   -> 12.5
float("12,5")   -> Ошибка
float("abc")    -> Ошибка
float(True)     -> 1.0
float(False)    -> 0.0

# 2.3 Логические значения (любое ненулевое значение переводится в True, любое нулевое в False)
bool(0)         -> False
bool(123)       -> True
bool(-23)       -> True
bool("")        -> False
bool("sdjhgf")  -> True

# 2.4 Строки
str(324)    -> "324"
str(-32)    -> "-32"
str(True)   -> "True"
str(43.2)   -> "43.2"

# 3. Операции над данными
# 3.1 Арифметические операции
# Сложение
int + int = int
float + int = float
int + float = float
float + float = float

# Вычитание
int - int = int
float - int = float
int - float = float
float - float = float

# Умножение
int * int = int
float * int = float
int * float = float 
float * float = float

# Деление
int / int = float
float / int = float
int / float = float
float / float = float 

# Возведение в степень
int ** int = int/float
float ** int = float
int ** float = float 

# Деление нацело (в результате остается ТОЛЬКО целая часть, результат НЕ округляется)
int // int = int
float // int = int
int // float = int 

# Взятие остатка
int % int = int
float % int = int
int % float = int

# 3.2 Арифметические операции сравнения
int > int  = bool 
int >= int = bool 
int < int  = bool 
int <= int = bool 
int == int = bool 
int != int = bool

# 3.3 Логические операции
bool and bool
# A B and
# 1 1  1
# 1 0  0
# 0 1  0
# 0 0  0

bool or bool
# A B or
# 1 1 1
# 1 0 1
# 0 1 1
# 0 0 0

not bool
# A not
# 1  0
# 0  1

# 3.4 Строковые операции
str + str = str # "abc" + "def" = "abcdef"
str * int = str # "abc" * 3 = "abcabcabc"
len(str) = int  # len("abcdef") = 6

# 4. Переменные
# Переменная — именованное хранилище для данных
# name = любое значение
a = 10
b = "10"
c = a + int(b)
d = str(a) + b

# 5. Базовые функции
print() # Вывод на экран
input() # Получить ввод от пользователя из консоли

# Пользователь вводит два числа, необходимо вывести на экран их сумму
a = int(input())
b = int(input())
print(a + b)
print(a + b)


