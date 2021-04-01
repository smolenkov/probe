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
class Element():                  # вода

    def __init__(self, name, liquidity, temperature, weight):
        self.name = name
        self.liquidity = liquidity          # текучесть
        self.temperature = temperature      # температура
        self.weight = weight                # вес
        self.new_name = None

    def sum(self, liquiditi, temperature, weight):
        self.liquidity = (liquiditi + self.liquidity)/2
        self.temperature = (temperature + self.temperature)/2
        self.weight = (weight + self.weight)/2
        if (self.liquidity >= 100) & (self.weight >= 45.5) & (self.temperature>=20):
            self.new_name = 'шторм'
        elif (self.liquidity >= 50) & (self.weight >= 155):
            self.new_name = 'пар'
        elif (self.liquidity >= 50) & (self.temperature >= 155):
            self.new_name = 'грязь'





elements = [Element(name = 'вода', liquidity = 100, temperature = 10, weight =90),
            Element(name = 'воздух', liquidity = 100, temperature = 30, weight =1),
            Element(name = 'огонь', liquidity = 0, temperature = 300, weight =0),
            Element(name = 'земля', liquidity = 0, temperature = 20, weight =100)]

while True:
    ingredient1 = random.choise(elements)
    ingredient2 = random.choise(elements)


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
