# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import create_snow, snow_draw, snow_clear, checking_y_snow, delete_snow, snow_shift
sd.resolution = (1200,800)
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)

while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    snow_counter = 10
    create_snow(snow_counter)

    for i in range (snow_counter):
        snow_draw(i)
    while snow_counter > 0:
        for i in range(snow_counter):
            snow_clear(i)
            snow_shift(i)
            snow_draw(i)
            # sd.sleep(0.01)
            if checking_y_snow(i) == False:
                delete_snow(i)
                snow_counter -=1
                break
        if sd.user_want_exit():
            break
    if sd.user_want_exit():
        break



    #  сдвинуть_снежинки()

    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    # sd.sleep(0.1)

# While True:
#     for i in range(coin_snow-1):
#         snow_clear(x=x_snow[i], y=y_snow[i], len=len_snow[i])
#         # sd.sleep(0.1)
#         if y_snow[i] <= 30:
#             snow_draw(x=x_snow[i], y=y_snow[i], len=len_snow[i])
#             x_snow[i] = randint(20, 1180)
#             y_snow[i] = 820
#             len_snow[i] = randint(10, 30)
#             speed_snow[i] = randint(1, 10)
#
#         y_snow[i] -= speed_snow[i]
#         snow_draw(x=x_snow[i], y=y_snow[i], len=len_snow[i])
#         # sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
sd.pause()
