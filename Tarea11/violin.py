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
    ax.set_xlabel('Funciones Objetivos')


# create test data
url_file = './data/tdonce.xlsx'



h1 = pd.read_excel(url_file,'Hoja1')
#Numeracion=h1['Numeracion'].tolist()

g2=h1['dos'].tolist()
g3=h1['tres'].tolist()
g4=h1['cuatro'].tolist()
g5=h1['cinco'].tolist()
g6=h1['seis'].tolist()
g7=h1['siete'].tolist()
g8=h1['ocho'].tolist()
g9=h1['nueve'].tolist()
g10=h1['diez'].tolist()
g11=h1['once'].tolist()
g12=h1['doce'].tolist()
data = [g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12]


#fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(9, 4), sharey=True)
fig1 = plt.figure(1, figsize=(9, 6))
ax2 = fig1.add_subplot(111)


ax2.set_ylabel('Porcentajes')
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
labels = ['2', '3', '4', '5','6','7','8','9','10','11','12']

set_axis_style(ax2, labels)

plt.subplots_adjust(bottom=0.15, wspace=0.05)
plt.show()