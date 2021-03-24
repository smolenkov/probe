# -*- coding: utf-8 -*-

import simple_draw as sd
import random as random

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
point = sd.get_point(300, 300)
radius = 100
for _ in range(3):
    sd.circle(point, radius=radius, width=2)
    radius += 5


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def circles(x , y , step, radius):
    point = sd.get_point(x , y)
    for _ in range(step):
        sd.circle(point, radius=radius, width=2)
        radius += 5

circles(500, 300, 50, 30)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

for i in range(10):
    point = sd.get_point(50 + i *10, 50 + i *5 )
    sd.circle(point, radius=50, width=2)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
for k in range(3):
    for i in range(10):
        point = sd.get_point(50 + i *10, 50 + k * 50 )
        sd.circle(point, radius=50, width=2)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range(5000):
    point = sd.random_point()
    color = sd.random_color()
    radius = int(random.random() * 30 + 10)
    sd.circle(point, radius, color, 2)
sd.pause()


