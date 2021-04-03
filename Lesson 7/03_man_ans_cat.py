# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.
class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print(f'{self.name} поел')
            self. fullness += 20
            self.house.food -= 10

    def game(self):
        print(f'{self.name} поиграл в PS 5')
        self.fullness -= 10

    def take_a_cat(self, cat, house):
        cat.house = house
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print(f'{self.name} сходил в магазин')
            self.house.money -= 50
            self.house.food += 50
            self.fullness -= 10
        else:
            print('Закончились деньги')

    def work(self):
        print(f'{self.name} сходил на работу')
        self.house.money +=30
        self.fullness -= 10


    def clean_house(self):
        print(f'{self.name} убрался в доме')
        if self.house.mud >= 10:
            self.house.mud -= 10
        self.fullness -= 10

    def man_act(self):
        if self.fullness <=0:
            print(f'{self.name} умер')
            return
        dice  = randint (1,4)
        if self.fullness <=20:
            self.eat()
        if self.house.food <=20:
            self.shopping()
        elif self.house.money <= 50:
            self. work()
        elif dice == 1:
            self.game()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.eat()
        else:
            self.clean_house()
        dice_cat = randint(1,20)


    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print(f'{self.name} Вьехал в дом')


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - кот {}, сытость {}'.format(self.name, self.fullness)

    def sleep(self):
        print(f'кот {self.name} поспал')
        self.fullness -= 10

    def eat(self):
        if self.house.food >= 10:
            print(f'кот {self.name} поел')
            self.fullness += 20
            self.house.food -= 10
        else:
            print('нет еды')

    def scratch(self):
        print(f'кот {self.name} поцарапал обои')
        self.fullness -= 10
        self.house.mud +=5

    def cat_act(self):
        if self.fullness <= 0:
            print(f'кот {self.name} умер')
            return
        dice = randint(1, 3)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.scratch()
        else:
            self.eat()

class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.mud = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, грязи {}'.format(self.food, self.money, self.mud)

citizens = [
    Man(name='Леонардо'),
    Man(name='Донателло'),
    Man(name='Микеланджело')]

cats = [Cat(name = 'Мурзик'),
        Cat(name = 'Барсик'),
        Cat(name = 'Персик')]

sweet_home = House()
i=0
for i in range(0,3):
    citizens[i].go_to_the_house(sweet_home)
    citizens[i].take_a_cat(cats[i], sweet_home)


for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.man_act()
    for cat in cats:
        cat.cat_act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for cat in cats:
        print(cat)
    print(sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
