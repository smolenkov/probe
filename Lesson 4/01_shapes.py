# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см Lesson 4/results/exercise_01_shapes.jpg

# TODO здесь ваш код
sd.resolution = (1200, 800)


def triangle(point, angle, len):
    v1 = sd.get_vector(start_point=point, angle=angle, length=len)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=len)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=len)
    v3.draw()

def square(point, angle, len):
    v1 = sd.get_vector(start_point=point, angle=angle, length=len)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=len)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=len)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=len)
    v4.draw()

def pentagon (point, angle, len):
    v1 = sd.get_vector(start_point=point, angle=angle, length=len)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=len)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=len)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=len)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=len)
    v5.draw()

# def octagon (point, angle, len):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=len)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=len)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=len)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=len)
#     v4.draw()
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=len)
#     v5.draw()
#     v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=len)
#     v6.draw()

def poligon (point, angle, len, coin):
    if coin < 2:
        return
    lock_point = point
    delta_angle = 360/coin
    for i in range (0, coin):
        v1 = sd.get_vector(start_point=point, angle=angle+delta_angle*i, length=len)
        v1.draw()
        point = v1.end_point
    sd.line(lock_point, v1.end_point)



point = sd.get_point(300 , 300)
poligon (point=point, angle = 45, len=150, coin = 5)

# for i in range (1, 361, 15):
#     triangle(point = point , angle = i , len =100)

# for i in range (1, 361, 45):
#     square(point = point , angle = i , len =100)

# for i in range (1, 361, 60):
#     pentagon(point = point , angle = i , len =100)

# for i in range (1, 361, 30):
#     octagon(point = point , angle = i , len =100)



# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
