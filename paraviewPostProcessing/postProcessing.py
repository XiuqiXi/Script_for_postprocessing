#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:26:17 2020

@author: xiuqi
"""

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from itertools import islice
import re

from matplotlib import rcParams
rcParams['font.family']='serif'
rcParams['font.sans-serif']=['Times New Roman']

f_condensed_phase = 'pyrolysisUpperPosition'
f_pyrolsysis_exp = 'pyrolysisLengthExperiment'
f_flame_length = 'flameLength'
f_flame_length_exp = 'flameLengthExp'

data_condensed_phase = np.loadtxt(f_condensed_phase)
data_pyrolysisExp = np.loadtxt(f_pyrolsysis_exp)
data_flame_length = np.loadtxt(f_flame_length)
data_flame_length_exp = np.loadtxt(f_flame_length_exp)


# plt.figure()
# plt.plot(data_condensed_phase[:,0], data_condensed_phase[:,1])
# plt.title('Preheat Length')
# plt.show()

# plt.figure()
# plt.plot(data_condensed_phase[:,0], data_condensed_phase[:,8])
# plt.title('B')
# plt.show()

# plt.figure()
# plt.plot(data_condensed_phase[:,0], data_condensed_phase[:,3])
# #plt.scatter(data_pyrolysisExp[:,0],data_pyrolysisExp[:,1])
# plt.title('Pyrolysis Position')
# plt.show()

# plt.figure()
# plt.plot(data_condensed_phase[:,0], data_condensed_phase[:,4])
# plt.title('Pyrolysis Increase')
# plt.show()

# plt.figure()
# plt.plot(data_condensed_phase[:,0], data_condensed_phase[:,5])
# plt.title('Heat Flux')
# plt.show()

# #plt.figure()
# #plt.plot(data_condensed_phase[:,0], data_condensed_phase[:,6])
# #plt.title('burn out position')

# plt.figure()
# plt.plot(data_flame_length[:, 0], data_flame_length[:, 1]-0.15)
# #plt.scatter(data_flame_length_exp[:, 0], data_flame_length_exp[:, 1])
# plt.title('flame length')
# plt.show()

plt.figure(figsize=(16,8))

plt.subplot(2, 3, 1)
plt.plot(data_condensed_phase[:,0], data_condensed_phase[:,3])
plt.title('Pyrolysis Position')

plt.subplot(2, 3, 2)
plt.plot(data_condensed_phase[:,0], data_condensed_phase[:,4])
plt.title('Pyrolysis Increase')

plt.subplot(2, 3, 3)
plt.plot(data_condensed_phase[:,0], data_condensed_phase[:,1])
plt.title('Preheat Length')

plt.subplot(2, 3, 4)
plt.plot(data_condensed_phase[:,0], data_condensed_phase[:,5])
plt.title('Heat Flux')

plt.subplot(2, 3, 5)
plt.plot(data_condensed_phase[:,0], data_condensed_phase[:,6])
plt.title('Burnout')

plt.subplot(2, 3, 6)
plt.plot(data_condensed_phase[:,0], data_condensed_phase[:,9]-data_condensed_phase[:,10])
# plt.plot(data_condensed_phase[:,0], data_condensed_phase[:,10])
plt.title('linearInterpolationLocation')
plt.ylim([-1.5,1.5])

plt.show()
