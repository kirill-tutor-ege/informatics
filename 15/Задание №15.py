# ДЕЛ(a, b) → (a % b == 0)
# ¬ДЕЛ(a, b) → (a % b != 0)
# x & y = z → (x & y == z)
# x ∈ A → (start<=x<=end)
# A = [start, end]

# !!!!!!! Важная пометка, значения диапазона range() зависят от формулировки задания
# Натуральное — 1, 2, … -> range(1, 100_000)
# Неотрицательное — 0, 1, 2, … -> range(100_000)
# Целое — …, -2, -1, 0, 1, 2, … -> range(-50_000, 50_000)

# Наименьший А, тождественно истинно
f = lambda x, A: ((x & 112 != 0) or (x & 86 != 0)) <= ((x & 65 == 0) <= (x & A != 0))
for A in range(1, 100):
    if all(f(x, A) for x in range(1, 100000)):
        print(A)
        break

# Наибольший А, тождественно истинно
f = lambda x, A: ((x & 112 != 0) or (x & 86 != 0)) <= ((x & 65 == 0) <= (x & A != 0))
for A in range(1, 10000):
    if all(f(x, A) for x in range(1, 100000)):
        print(A) # В ответ идет последнее число, выведенное на экран

# Наименьший А, истинно
f = lambda x, A: ((x & 112 != 0) or (x & 86 != 0)) <= ((x & 65 == 0) <= (x & A != 0))
for A in range(1, 100):
    if any(f(x, A) for x in range(1, 100000)):
        print(A)
        break

# Наибольший А, истинно
f = lambda x, A: ((x & 112 != 0) or (x & 86 != 0)) <= ((x & 65 == 0) <= (x & A != 0))
for A in range(1, 100):
    if any(f(x, A) for x in range(1, 100000)):
        print(A) # В ответ идет последнее число, выведенное на экран

# Наименьший А, тождественно ложно
f = lambda x, A: ((x & 112 != 0) or (x & 86 != 0)) <= ((x & 65 == 0) <= (x & A != 0))
for A in range(1, 100):
    if all(not f(x, A) for x in range(1, 100000)):
        print(A)
        break

# Наибольший А, тождественно ложно
f = lambda x, A: ((x & 112 != 0) or (x & 86 != 0)) <= ((x & 65 == 0) <= (x & A != 0))
for A in range(1, 100):
    if all(not f(x, A) for x in range(1, 100000)):
        print(A) # В ответ идет последнее число, выведенное на экран

# Наименьший А, ложно
f = lambda x, A: ((x & 112 != 0) or (x & 86 != 0)) <= ((x & 65 == 0) <= (x & A != 0))
for A in range(1, 100):
    if any(not f(x, A) for x in range(1, 100000)):
        print(A)
        break

# Наибольший А, ложно
f = lambda x, A: ((x & 112 != 0) or (x & 86 != 0)) <= ((x & 65 == 0) <= (x & A != 0))
for A in range(1, 100):
    if any(not f(x, A) for x in range(1, 100000)):
        print(A) # В ответ идет последнее число, выведенное на экран

# Если у нас x и y
f = lambda x, y, A: логическая функция из задания
for A in range(1, 100):
    if all(f(x, y, A) for x in range(1, 10000) for y in range(1, 10000)):
        print(A)

# Отрезки
for start in 25, 32, 47, 50:
    for end in 25, 32, 47, 50:
        if start < end:
            f = lambda x: ((not(start<=x<=end)) <= (25<=x<=50)) <= ((start<=x<=end) <= (32<=x<=47))
            if all(f(x) for x in [10, 27, 40, 48, 55]):
                print(end - start)


