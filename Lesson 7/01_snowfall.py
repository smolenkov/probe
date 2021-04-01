# -*- coding: utf-8 -*-
from random import randint
import simple_draw as sd
sd.resolution = (1200,800)

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.x_snow = randint(20, 1180)
        self.y_snow = 770
        self.len_snow = randint(10, 30)
        self.delta_x_snow = randint(0, 2)
        self.delta_y_snow = randint(7, 10)
        self.color_snow = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.down_snow = 0

    def snow_draw(self):
        self.point = sd.get_point(self.x_snow, self.y_snow)
        sd.snowflake(center=self.point, length=self.len_snow, color=self.color_snow)

    def snow_clear(self):
        self.point = sd.get_point(self.x_snow, self.y_snow)
        self.color_clear = sd.background_color
        sd.snowflake(center=self.point, length=self.len_snow, color=self.color_clear)

    def snow_shift(self):
        self.x_snow += randint(-2, 2)
        self.y_snow -= self.delta_y_snow

    def checking_fall(self):
        if self.y_snow < 20:
            self.down_snow = 1
            return False


flakes = []
for _ in range (30):
    flakes.append(Snowflake())

while True:
    for flake in flakes:
        flake.snow_clear()
        flake.snow_shift()
        flake.snow_draw()
        flake.checking_fall()
        if flake.down_snow == 1:
            flakes.remove(flake)
            flakes.append(Snowflake())
            break
        sd.sleep(0.001)
        if sd.user_want_exit():
            break
    if sd.user_want_exit():
        break
# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок

# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
