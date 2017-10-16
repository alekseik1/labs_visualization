import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from scipy.interpolate import interp1d
import pandas as pd

input_file = './sample_input.txt'

x_data = 'I'
y_data = 'V'

start_x_with_zero = False
start_y_with_zero = False

frame = pd.read_csv(input_file)

x = frame[[x_data]]
y = frame[[y_data]]

y_max = np.max(y)[0]
y_min = np.min(y)[0]
x_max = np.max(x)[0]
x_min = np.min(x)[0]


def por(x):
    if x == 0:
        return 10**-7
    return int(np.floor(np.log10(np.abs(x))))

# TODO: Князев любит, когда major ticks начинабтся с целого числа и заканчиваются на максимальном значении (целое, то есть надо округлять).
# TODO: Переделать это. Пока в notebook поставлю ручную заглушку
def best_tick_interval(x_max, x_min):
    delta_p = 10**por(x_max - x_min)
    v = [1, 2, 4, 5, 8,]
    for k in v:
        if(2 < np.floor((x_max*1.1 - x_min)/(k*delta_p))+1 < 10):
            return k*delta_p

'''
major_x_ticks_variants = np.arange(por(x_min), por(x_max) * 1.01, 2 * 10 ** por(x_min))
major_y_ticks_variants = np.arange(por(y_min), por(y_max) * 1.01, 2 * 10 ** por(y_min))

# Ищем лучший вариант для major_ticks

best_x_variant = major_x_ticks_variants[0]
best_y_variant = major_y_ticks_variants[0]

for variant in major_x_ticks_variants:
    if 5 < (x_max - x_min) / variant <= 9:
        best_x_variant = variant
        break

for variant in major_y_ticks_variants:
    if 5 < (y_max - y_min) / variant <= 9:
        best_y_variant = variant
        break

print(best_x_variant)
print(best_y_variant)
'''

best_x_variant = best_tick_interval(x_max, x_min)
best_y_variant = best_tick_interval(y_max, y_min)
print(best_x_variant, best_y_variant)

xmajorLocator = MultipleLocator(best_x_variant)
ymajorLocator = MultipleLocator(best_y_variant)

number_of_minor_ticks = 4   # Лучше так и оставить

xminorLocator = MultipleLocator(best_x_variant / number_of_minor_ticks)
yminorLocator = MultipleLocator(best_y_variant / number_of_minor_ticks)

fig, ax = plt.subplots(dpi=500)

# set Locators
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

ax.plot(x, y, '-', color='k')

ax.grid(which='major', ls='-', lw=0.5, c='k', alpha=0.9)
ax.grid(which='minor', ls='--', lw=0.5, c='grey', alpha=0.9)

plt.savefig("out_graph.png")
plt.show()
