# Подлючаем черепаху  
from turtle import *

# Задаем скорость рисования (0 - без анимации(P.S. Моментально))
tracer(0)
# Задаем масштаб рисунка (больше масштаб - больше рисунок)
m = 15
screensize(3000, 3000)
# Выравниваем по оси ординат (Где это необходимо)
left(90)

# повтори k раз
for _ in range(k):

# переписываем алгоритм
left(30) # Поворот влево (передаем угол в градусах)
forward(10 * m) # Идти вперед (передаем число, умноженное на масштаб)
right(45) # Поворот вправо (передаем угол в градусах)
back(30 * m) # Идти назад (передаем число, умноженное на масштаб)
pendown() # Опустить хвост(начинает оставлять след от своего движения)
penup() # Поднять хвост

# Краткие варианты предыдущих комнд
lt(30) # Поворот влево (передаем угол в градусах)
fd(10 * m) # Идти вперед (передаем число, умноженное на масштаб)
rt(45) # Поворот вправо (передаем угол в градусах)
bk(30 * m) # Идти назад (передаем число, умноженное на масштаб)
down() # Опустить хвост(начинает оставлять след от своего движения)
up() # Поднять хвост

# Поднимаем хвост
penup()
# Ставим красные точки на целых значениях координат
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m) # Переходим в позицию x, y
        dot(3) # Ставим точку радиуса 3

done() # Конец программы




# TODO
from turtle import *

tracer(0)
corners1, corners2 = set(), set()

for _ in range(5):
    forward(37)
    corners1.add((round(xcor()), round(ycor())))
    right(90)
    forward(44)
    corners1.add((round(xcor()), round(ycor())))
    right(90)
up()
back(18)
right(90)
forward(29)
left(90)
down()
for _ in range(5):
    forward(31)
    corners2.add((round(xcor()), round(ycor())))
    right(90)
    forward(35)
    corners2.add((round(xcor()), round(ycor())))
    right(90)

def rectangle(corners):
    x_min, y_min = map(min, zip(*corners))
    x_max, y_max = map(max, zip(*corners))
    return set((x, y) for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1))

rectangle1 = rectangle(corners1)
rectangle2 = rectangle(corners2)

print(len(rectangle1 & rectangle2))