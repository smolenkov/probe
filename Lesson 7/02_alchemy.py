# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
import copy
from random import choice, random, randint


class Element():

    def __init__(self, name=None, liquidity=None, temperature=None, weight=None):
        self.name = name
        self.liquidity = liquidity
        self.temperature = temperature
        self.weight = weight
        self.new_name = None

    def sum(self, liquidity_add, temperature_add, weight_add):
        self.liquidity = (liquidity_add + self.liquidity) / 2
        self.temperature = (temperature_add + self.temperature) / 2
        self.weight = (weight_add + self.weight) / 2
        # print(f'L -{self.liquidity} W -{self.weight} T -{self.temperature}')
        if (self.liquidity == 100) & (self.temperature== 20) & (self.weight == 45.5):
            self.new_name = 'шторм'
        elif (self.liquidity == 50) & (self.temperature == 155) & (self.weight == 45):
            self.new_name = 'пар'
        elif (self.liquidity == 50) & (self.temperature == 15) & (self.weight == 95):
            self.new_name = 'грязь'
        elif (self.liquidity == 50) & (self.temperature == 165) & (self.weight == 0.5):
            self.new_name = 'молния'
        elif (self.liquidity == 50) & (self.temperature == 25) & (self.weight == 50.5):
            self.new_name = 'пыль'
        elif (self.liquidity == 0) & (self.temperature == 160) & (self.weight == 50):
            self.new_name = 'лава'
        self.name = self.new_name


main_elements = [Element(name='вода', liquidity=100, temperature=10, weight=90),
                 Element(name='воздух', liquidity=100, temperature=30, weight=1),
                 Element(name='огонь', liquidity=0, temperature=300, weight=0),
                 Element(name='земля', liquidity=0, temperature=20, weight=100)]

list_elements = []
for i in main_elements:
    print(i.name)
for i in range(10):
    while True:
        ingredient_1 = copy.deepcopy(main_elements[randint(0,3)])
        name = ingredient_1.name
        ingredient_2 = copy.deepcopy(main_elements[randint(0,3)])
        if ingredient_1.name != ingredient_2.name:
            break
    ingredient_1.sum(liquidity_add=ingredient_2.liquidity, temperature_add=ingredient_2.temperature,
                     weight_add=ingredient_2.weight)
    list_elements.append(ingredient_1)
    # print(f'создано {i + 1}элементов')
    # print(list_elements)
    print(name, ' + ', ingredient_2.name, ' = ', ingredient_1.name)
    print("----------------------------------")
    # print(list_elements)
# for i in (list_elements):
#     print(i.name)



# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
