# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd

sd.resolution = (1200,800)
import simple_draw as sd
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
def snowfall():
    x_snow = []
    y_snow = []
    len_snow = []
    coin_iteration = []
    coin_snow = 10 # количество снежинок
    speed_snow = []
    for i in range (coin_snow-1):
        x_snow.insert(i, randint(20, 600)) # первоначальное размещение снежинок вверху по горизонтали
        y_snow.insert(i, 830) # высота первоначального размещения снежинок
        len_snow.insert(i, randint(10, 30)) # длина лучей снежинки
        speed_snow.insert(i, randint(1, 10)) #  смещение снежинки вниз на каждом шаге
        coin_iteration.insert(i, 3) # количество падений каждой снежинки


    def snow_draw(x, y, len): #  отрисовка снежинки
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=len)


    def snow_clear(x, y, len): #  закрашивание снежинки
        point = sd.get_point(x, y)
        color_clear = sd.background_color
        sd.snowflake(center=point, length=len, color=color_clear)


    while True:
        for i in range(coin_snow-1):
            snow_clear(x=x_snow[i], y=y_snow[i], len=len_snow[i])
            # sd.sleep(0.1)
            if y_snow[i] <= 30: # высота на которой снежинка останавливается
                snow_draw(x=x_snow[i], y=y_snow[i], len=len_snow[i])
                coin_iteration[i] -= 1
                x_end, y_end, len_end = x_snow, y_snow, len_snow
                x_snow[i] = randint(20, 600)
                y_snow[i] = 830
                len_snow[i] = randint(10, 30)
                speed_snow[i] = randint(1, 10)
                if coin_iteration[i] <= 0:
                    speed_snow[i] = 0
                    x_snow, y_snow, len_snow = x_end, y_end, len_end
            y_snow[i] -= speed_snow[i]
            snow_draw(x=x_snow[i], y=y_snow[i], len=len_snow[i])
            # sd.sleep (0.1)
        # print('coin_iteration - ', coin_iteration)
        # print('speed_snow - ', speed_snow)
        # print(set(speed_snow))
        if sd.user_want_exit():
            break
        if set(speed_snow) == {0}:
            sd.sleep(3)
            break


    # sd.pause()
a = snowfall()

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


