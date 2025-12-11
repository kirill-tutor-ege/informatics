def move(s):
  a, b = s
  return [a + 1, b], [a, b + 1], [a * 2, b], [a, b * 2]

def end(s):
  return sum(s) > 117

def win1(n):
  return any(end(x) for x in move(n)) and not end(n)

def lose1_fail(n):
  return any(win1(x) for x in move(n))

def lose1(n):
  return all(win1(x) for x in move(n))

def win2(n):
  return any(lose1(x) for x in move(n)) and not win1(n)

def lose12(n):
  return all(win1(x) or win2(x) for x in move(n)) and not lose1(n)

print("19: ", [x for x in range(1, 115 + 1) if lose1([7, x])]) # lose1_fail, если в 19-ом неудачный ход
print("20: ", [x for x in range(1, 115 + 1) if win2([7, x])])
print("21: ", [x for x in range(1, 115 + 1) if lose12([7, x])])
