# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd

sd.resolution = (1500, 1200)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,
def draw_branches(point, angle, length, width1):
    if length < 0:
        return
    v1 = sd.get_vector(start_point = point, angle = angle, length=length, width=int(width1))
    v1.draw()
    point = v1.end_point
    delta = randint(5, 25)
    angle = angle - delta
    length = length - delta * 0.5
    angle1 = angle + 2 * delta
    width1 = width1 * 0.85
    draw_branches(point, angle, length, width1)
    draw_branches(point, angle1, length, width1)

start_point = sd.get_point (700, 0)
angle = 90
length = 121
width = 8
draw_branches(point=start_point, angle=angle, length=length, width1 = width)


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см Lesson 4/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см Lesson 4/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


