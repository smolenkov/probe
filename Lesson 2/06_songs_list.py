#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
dict_violator_song = {violator_songs_list[i][0] : violator_songs_list[i][1] for i in range(0 , len(violator_songs_list))} #list -> dictionary

time_halo = dict_violator_song['Halo']
time_Enjoy = dict_violator_song['Enjoy the Silence']
time_Clean = dict_violator_song['Clean']

summary_time = time_halo + time_Enjoy + time_Clean

print(f'Три песни звучат {round(summary_time , 2)} минут')



# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# TODO здесь ваш код

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# TODO здесь ваш код
time_Sweetest = violator_songs_dict['Sweetest Perfection']
time_Policy = violator_songs_dict['Policy of Truth']
time_Blue = violator_songs_dict['Blue Dress']

summary_time1 = time_Sweetest + time_Policy + time_Blue

print(f'Другие три песни звучат {round(summary_time1 , 2)} минут')