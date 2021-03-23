#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)
#
print(garden_set)
print(meadow_set)
# выведите на консоль все виды цветов
#

# выведите на консоль те, которые растут и там и там
#
summary_set = garden_set & meadow_set
print(f'И там и там ростут: {summary_set}')
# выведите на консоль те, которые растут в саду, но не растут на лугу
#
only_garden_set = garden_set - meadow_set
print(f'Только в саду ростут: {only_garden_set}')
# выведите на консоль те, которые растут на лугу, но не растут в саду
#
only_meadow_set = meadow_set - garden_set
print(f'Только на лугу ростут: {only_meadow_set}')

