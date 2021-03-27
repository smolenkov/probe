# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 800)

# Добавить цвет в функции рисования геом. фигур. из упр Lesson 4/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см Lesson 4/results/exercise_02_global_color.jpg
# def vector(start, angle, length, color=COLOR_YELLOW, width=1):
#
#         Нарисовать вектор цветом color толщиной width
#         Из точки start
#         В направлении angle
#         Длиной length
# COLOR_WHITE = (255, 255, 255)
# COLOR_BLACK = (0, 0, 0)
#
# COLOR_RED = (255, 0, 0)
# COLOR_ORANGE = (255, 127, 0)
# COLOR_YELLOW = (255, 255, 0)
# COLOR_GREEN = (0, 255, 0)
# COLOR_CYAN = (0, 255, 255)
# COLOR_BLUE = (0, 0, 255)
# COLOR_PURPLE = (255, 0, 255)
#
# COLOR_DARK_YELLOW = (127, 127, 0)
# COLOR_DARK_ORANGE = (127, 63, 0)
# COLOR_DARK_RED = (127, 0, 0)
# COLOR_DARK_GREEN = (0, 127, 0)
# COLOR_DARK_CYAN = (0, 127, 127)
# COLOR_DARK_BLUE = (0, 0, 127)
# COLOR_DARK_PURPLE = (127, 0, 127)

# TODO здесь ваш код
def poligon (point, angle, len, coin, color):
    if coin < 2:
        return
    sd.invert_color(color)
    sd.invert_color(color)
    lock_point = point
    delta_angle = 360/coin
    print(color)
    for i in range (0, coin):
        v1 = sd.get_vector(start_point=point, angle=angle+delta_angle*i, length=len)
        # v1.draw()
        sd.line(point, v1.end_point, color=color, width=3)
        point = v1.end_point
    sd.line(lock_point, v1.end_point, color = color, width=3)



point_start = sd.get_point(300 , 300)
coin = int(input('Введите количество вершин'))
col = int(input('Введите номер цвета: 1-RED, 2-ORANGE, 3-YELLOW, 4-GREEN, 5-CYAN, 6-BLUE, 7-PURPLE '))
colors = {
          1 : (255, 0, 0),
          2 : (255, 127, 0),
          3 : (255, 255, 0),
          4 : (0, 255, 0),
          5 : (0, 255, 255),
          6 : (0, 0, 127),
          7 : (127, 0, 127)
          }
color = colors[col]
# color=sd.random_color()
poligon (point=point_start, angle = 45, len=150, coin = coin, color = color)

sd.pause()
