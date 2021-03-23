#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код
amount_words = my_favorite_movies.count(',') +1 # количество слов
amount_letters = len(my_favorite_movies) # длина списка
numbers_commas = []
for i in range (amount_letters): # поиск запятых в списке фильмов
    if my_favorite_movies[i] == ",":
        numbers_commas.append(i) # список  порядковых номеров запятых
print (my_favorite_movies)
print (f'слов:{amount_words} , запятые: {numbers_commas})')
print (f'первый фильм {my_favorite_movies[:numbers_commas[0]]}')
print (f'последний фильм {my_favorite_movies[numbers_commas[len(numbers_commas)-1]+1:]}')
print (f'второй фильм {my_favorite_movies[numbers_commas[0]+1:numbers_commas[1]]}')
print (f'второй с конца {my_favorite_movies[numbers_commas[len(numbers_commas)-2]+1 : numbers_commas[len(numbers_commas)-1]]}')

print(len(numbers_commas))
print(numbers_commas[len(numbers_commas)-1])




