# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 16:15:33 2022

@author: cege
"""


import numpy as np


f_condensed_phase = 'pyrolysisUpperPosition'
data_condensed_phase = np.loadtxt(f_condensed_phase)

row_rand_array = np.arange(data_condensed_phase.shape[0])
np.random.shuffle(row_rand_array)
row_rand = data_condensed_phase[row_rand_array[0:50000]]

