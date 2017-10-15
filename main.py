import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from scipy.interpolate import interp1d
import pandas as pd

input_file = './sample_input.txt'
x_data = 'I'
y_data = 'V'


frame = pd.read_csv(input_file)

x = frame[[x_data]]
y = frame[[y_data]]

y_max = np.max(y)[0]
y_min = np.min(y)[0]
x_max = np.max(x)[0]
x_min = np.min(x)[0]

major_ticks_variants = [5 * 10 ** (n) for n in range(-8, 8)]

# Ищем лучший вариант для major_ticks (чтобы были через 5 и чтобы все изменерия там поместились)

best_x_variant = major_ticks_variants[0]
best_y_variant = major_ticks_variants[0]

for variant in major_ticks_variants:
    if 0 < (x_max - x_min) / variant <= 10:
        best_x_variant = variant
        break

for variant in major_ticks_variants:
    if 0 < (y_max - y_min) / variant <= 10:
        best_y_variant = variant
        break


xmajorLocator = MultipleLocator(best_x_variant)
ymajorLocator = MultipleLocator(best_y_variant)

number_of_ticks = 5

xminorLocator = MultipleLocator(best_x_variant / number_of_ticks)
yminorLocator = MultipleLocator(best_y_variant / number_of_ticks)


fig, ax = plt.subplots()

ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)


plt.plot(x, y, '--', color='k')
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')

plt.show()