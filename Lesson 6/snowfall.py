# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd

sd.resolution = (1200,800)
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

    for count in range (count_snow - 1):
        create_one_snow(count)

def create_one_snow (i):
    x_snow.insert(i, randint(20, 1180))
    y_snow.insert(i, 770)
    len_snow.insert(i, randint(10, 30))
    delta_x_snow.insert(i, randint(1, 5))
    delta_y_snow.insert(i, randint(1, 5))
    color_snow.insert(i, (randint(255), randint(255), randint(255)))


def snow_draw(x, y, len, color):
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=len)

def snow_clear(x, y, len):
    point = sd.get_point(x, y)
    color_clear = sd.background_color
    sd.snowflake(center=point, length=len, color=color_clear)

def checking_y_snow(y_snow, count_snow):
    if y_snow  < 20:
        down_snow[count_snow] = 1



while True:
    for i in range(coin_snow-1):
        snow_clear(x=x_snow[i], y=y_snow[i], len=len_snow[i])
        # sd.sleep(0.1)
        if y_snow[i] <= 30:
            snow_draw(x=x_snow[i], y=y_snow[i], len=len_snow[i])
            x_snow[i] = randint(20, 1180)
            y_snow[i] = 820
            len_snow[i] = randint(10, 30)
            speed_snow[i] = randint(1, 10)

        y_snow[i] -= speed_snow[i]
        snow_draw(x=x_snow[i], y=y_snow[i], len=len_snow[i])
        # sd.sleep(0.1)
    if sd.user_want_exit():
        break


sd.pause()

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


