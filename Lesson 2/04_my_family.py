#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['папа' , 'мама' , 'дочка' , 'собака']


# список списков приблизителного роста членов вашей семьи
my_family_height = ['Саша' , 182] , ['Лена' , 160] , ['Саша' , 162] , ['Рокки' , 70]

print (my_family_height)
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print(f'Рост отца -{my_family_height[0][1]} см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
len_list = len(my_family_height)
sum_height = 0
print(len_list)
for i in range(len_list):
    sum_height = sum_height + int(my_family_height[i][1])
    #print(int((my_family_height[i][1])))

print (f'Общий рост семьи: {sum_height} см')