# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200 , 800)
import random
# (определение функций)
import simple_draw

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x ,y , color):
    point = sd.get_point(x , y)
    point_left = sd.get_point( x - 20, y + 10)
    point_right = sd.get_point( x + 20, y + 10)
    point_left_mouth = sd.get_point( x - 50, y - 30)
    point_right_mouth = sd.get_point( x + 50, y - 30)
    sd.circle(point, 100, color, 2)
    sd.circle(point_left, 10, color, 4)
    sd.circle(point_right, 10, color, 4)
    sd.line(point_left_mouth , point_right_mouth , color , 5)


color = sd.random_color()
x , y = 150 , 150
smile (x , y , color)
for _ in range(30):
    x = int(random.random() * 1000 + 100)
    y = int(random.random() * 600 + 100)
    color = sd.random_color()
    smile(x, y, color)

sd.pause()
