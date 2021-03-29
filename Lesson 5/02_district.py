# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код

from district.central_street.house1.room1 import folks as room1_1
from district.central_street.house1.room2 import folks as room1_2
from district.central_street.house2.room1 import folks as room2_1
from district.central_street.house2.room2 import folks as room2_2
print('На районе живут: ',','.join((room1_1+room1_2+room2_1+room2_2)))
# print(room1_1.folks)
# print(room1_2.folks)
# print(room2_1.folks)
# print(room2_2.folks)

# import os
# tree = (os.walk('.'))
# for i in tree:
#     print( i )
# # Set the directory you want to start from
# rootDir = '.'
# for dirName, subdirList, fileList in os.walk(rootDir):
#     print('Found directory: %s' % dirName)
#     for fname in fileList:
#         print('\t%s' % fname)
