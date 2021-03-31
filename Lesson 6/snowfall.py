# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd

#sd.resolution = (1200,800)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
def create_snow(count_snow):
    from random import randint

    global x_snow, y_snow, len_snow, delta_x_snow, delta_y_snow, color_snow, down_snow
    x_snow, y_snow, len_snow, delta_x_snow, delta_y_snow, color_snow, down_snow = [],[],[],[],[],[],[]
    count_snow = count_snow

    for count in range (count_snow):
        create_one_snow(count)
    # print('x-', x_snow)

def create_one_snow (i):
    x_snow.insert(i, randint(20, 1180))
    y_snow.insert(i, 770)
    len_snow.insert(i, randint(10, 30))
    delta_x_snow.insert(i, randint(0, 2))
    delta_y_snow.insert(i, randint(3, 5))
    color_snow.insert(i, (randint(0, 255), randint(0, 255), randint(0, 255)))
    down_snow.insert(i,0)

def snow_shift(i):
    # print(x_snow[i], delta_x_snow[i])
    x_snow[i] = x_snow[i] + delta_x_snow[i]
    y_snow[i] = y_snow[i] - delta_y_snow[i]


def snow_draw(i):
    # print('snow_draw[',i,'] - ', x_snow)
    x = x_snow[i]
    y = y_snow[i]
    len = len_snow[i]
    color = color_snow[i]
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=len, color = color)

def snow_clear(i):
    # print('snow_clear[',i,'] - ', x_snow)
    x = x_snow[i]
    y = y_snow[i]
    len = len_snow[i]
    point = sd.get_point(x, y)
    color_clear = sd.background_color
    sd.snowflake(center=point, length=len, color=color_clear)

def checking_y_snow(i):
    if y_snow[i]  < 20:
        down_snow[i] = 1
        return False

def delete_snow(i):
    # print('before delete_draw[',i,'] - ', x_snow)
    x_snow.pop(i)
    y_snow.pop(i)
    len_snow.pop(i)
    delta_x_snow.pop(i)
    delta_y_snow.pop(i)
    color_snow.pop(i)
    down_snow.pop(i)
    # print('after delete_draw[', i, '] - ', x_snow)

# sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


