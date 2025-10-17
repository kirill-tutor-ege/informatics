def move(s):
  a, b = s
  return [a + 1, b], [a, b + 1], [a * 2, b], [a, b * 2]

def end(s):
  return sum(s) > 117

def win1(s):
  return any(end(x) for x in move(s))

def lose1_fail(s):
  return any(win1(x) for x in move(s)) and not all(end(x) for x in move(s))

def lose1(s):
  return all(win1(x) for x in move(s)) and win1(s) == False

def win2(s):
  return any(lose1(x) for x in move(s)) and win1(s) == False

def lose12(s):
  return all(win1(x) or win2(x) for x in move(s)) and not all(win1(x) for x in move(s))

print("19: ", [x for x in range(1, 115 + 1) if lose1([7, x])]) # lose1_fail, если в 19-ом неудачный ход
print("20: ", [x for x in range(1, 115 + 1) if win2([7, x])])
print("21: ", [x for x in range(1, 115 + 1) if lose12([7, x])])