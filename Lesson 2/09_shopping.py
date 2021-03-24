#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами
from pprint import pprint
shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}
'''
list_shops = list(shops.keys())
amound_shops=len(list_shops)
print (f'Магазинов-{amound_shops} : {list_shops}') # список магазинов
for i in range(len(list_shops)): # перебираем магазины
    print(i, list_shops[i])
    for y in range(len(list_shops[i])):
        produkt_keys = list((shops[list_shops[i]][y]).keys())
        for z in range(len(shops[list_shops[i]][y])):
            print(shops[list_shops[i]][y][produkt_keys[z]])
            #print(i ,y , z, produkt_keys[z])


#print (shops['ашан'].keys())
#print(shops[list_shops[0]])
'''
# Создайте словарь цен на продукты следующего вида (писать прямо в коде)

sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 9.99},
        {'shop': 'пятерочка', 'price': 10.99},

    ],
    'конфеты': [
        {'shop': 'ашан', 'price': 29.99},
        {'shop': 'пятерочка', 'price': 39.99},

    ],

}
# Указать надо только по 2 магазина с минимальными ценами


