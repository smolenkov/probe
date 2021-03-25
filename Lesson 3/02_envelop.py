# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные
'''
envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
# проверить для
paper_x, paper_y = 9, 8
paper_x, paper_y = 6, 8
paper_x, paper_y = 8, 6
paper_x, paper_y = 3, 4
paper_x, paper_y = 11, 9
paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)
answer = 'Не поместится'

print(f'x-{paper_x} y-{paper_y}')
if envelop_x > paper_x: # Проверка горизонтальнрого вхождения бумаги
    if envelop_y > paper_y:
        answer = 'Поместится'
if envelop_x > paper_y: # Проверка вертикального вхождения бумаги (повернули бумагу на 90 градусов)
    if envelop_y > paper_x:
        answer = 'Поместится'
print(answer)

'''
# TODO здесь ваш код

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 11, 10, 2
brick_x, brick_y, brick_z = 11, 2, 10
brick_x, brick_y, brick_z = 10, 11, 2
brick_x, brick_y, brick_z = 10, 2, 11
brick_x, brick_y, brick_z = 2, 10, 11
brick_x, brick_y, brick_z = 2, 11, 10
brick_x, brick_y, brick_z = 3, 5, 6
brick_x, brick_y, brick_z = 3, 6, 5
brick_x, brick_y, brick_z = 6, 3, 5
brick_x, brick_y, brick_z = 6, 5, 3
brick_x, brick_y, brick_z = 5, 6, 3
brick_x, brick_y, brick_z = 5, 3, 6
brick_x, brick_y, brick_z = 11, 3, 6
brick_x, brick_y, brick_z = 11, 6, 3
brick_x, brick_y, brick_z = 6, 11, 3
brick_x, brick_y, brick_z = 6, 3, 11
brick_x, brick_y, brick_z = 3, 6, 11
brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)

answer_brick = 'Не поместится'
print(f'отверстие  x-{hole_x}  y-{hole_y}')
print(f'x-{brick_x} y-{brick_y} z-{brick_z}')
if hole_x > brick_x: # Проверка горизонтальнрого вхождения кирпича
    if hole_y > brick_y:
        answer_brick = 'Поместится'
if hole_x > brick_y: # Проверка горизонтального повернутого вхождения кирпича
    if hole_y > brick_x:
        answer_brick = 'Поместится'
if hole_x > brick_x: # Проверка продольного вхождения кирпича
    if hole_y > brick_z:
        answer_brick = 'Поместится'
if hole_x > brick_z: # Проверка продольного повернутого вхождения кирпича
    if hole_y > brick_x:
        answer_brick = 'Поместится'
if hole_x > brick_z: # Проверка вертикальгного вхождения кирпича
    if hole_y > brick_y:
        answer_brick = 'Поместится'
if hole_x > brick_y: # Проверка вертикальгного повернутого вхождения кирпича
    if hole_y > brick_z:
        answer_brick = 'Поместится'



print(answer_brick)