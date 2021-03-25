# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (1200 , 800)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
radius = (300**2+400**2)**0.5*0.5
point = sd.get_point(200 , 250)
for i in range (len(rainbow_colors)):
    sd.circle(center_position = point , radius = (radius + (i * 5)) , color = rainbow_colors[i], width = 4 )

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
def progr ( num ):
    for _ in range (num):
        num += num * 0.9
    return (int(num))
radius = 10
point = sd.get_point(1200, 0)
for i in range (len(rainbow_colors), 0 , -1):
    sd.circle(center_position = point , radius = radius + progr(i) , color = rainbow_colors[i-1], width = progr(i) )
    print(progr(i))

sd.pause()
