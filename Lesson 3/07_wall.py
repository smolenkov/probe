# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
shift = 50
color = sd.COLOR_YELLOW
sd.resolution = (1200 , 800)
start_x = 1
start_y = 1
width = 2
for y in range(start_y, 801, 50):
    start_x = start_x * (-1)
    for x in range (start_x * 50 ,1201, 100):
        left_bottom_point = sd.get_point(x , y)
        right_top_point = sd.get_point(x+100 , y+50)
        print(left_bottom_point , right_top_point)
        sd.rectangle(left_bottom_point, right_top_point , color=color , width=width)


sd.pause()
