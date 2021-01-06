# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:32:08 2020
@author: Admin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def adjacent_values(vals, q1, q3):
    upper_adjacent_value = q3 + (q3 - q1) * 1.5
    upper_adjacent_value = np.clip(upper_adjacent_value, q3, vals[-1])

    lower_adjacent_value = q1 - (q3 - q1) * 1.5
    lower_adjacent_value = np.clip(lower_adjacent_value, vals[0], q1)
    return lower_adjacent_value, upper_adjacent_value


def set_axis_style(ax, labels):
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Cantidad de nodos')


# create test data
url_file = './data/Resumen_res.xlsx'



h1 = pd.read_excel(url_file,'latencia')
#Numeracion=h1['Numeracion'].tolist()
g2=h1['10_A'].tolist()
g3=h1['10_B'].tolist()
g4=h1['10_C'].tolist()
g5=h1['20_A'].tolist()
g6=h1['20_B'].tolist()
g7=h1['20_C'].tolist()
g8=h1['50_A'].tolist()
g9=h1['50_B'].tolist()
g10=h1['50_C'].tolist()
data = [g2,g3,g4,g5,g6,g7,g8,g9,g10]


#fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(9, 4), sharey=True)
fig1 = plt.figure(1, figsize=(9, 6))
ax2 = fig1.add_subplot(111)


ax2.set_ylabel('Latencia')
ax2.violinplot(data)


parts = ax2.violinplot(
        data, showmeans=False, showmedians=False,
        showextrema=False)

for pc in parts['bodies']:
    pc.set_facecolor('#D43F3A')
    pc.set_edgecolor('black')
    pc.set_alpha(1)

quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)
whiskers = np.array([
    adjacent_values(sorted_array, q1, q3)
    for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
whiskers_min, whiskers_max = whiskers[:, 0], whiskers[:, 1]

inds = np.arange(1, len(medians) + 1)
ax2.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
ax2.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
ax2.vlines(inds, whiskers_min, whiskers_max, color='k', linestyle='-', lw=1)

# set style for the axes
labels = ['10_A', '10_B', '10_C', '20_A', '20_B', '20_C','50_A', '50_B', '50_C']

set_axis_style(ax2, labels)

plt.subplots_adjust(bottom=0.15, wspace=0.05)
plt.show()
