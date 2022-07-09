# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 11:12:55 2022

@author: cege
"""

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from itertools import islice
import re

from matplotlib import rcParams
rcParams['font.family']='serif'
rcParams['font.sans-serif']=['Times New Roman']

f_condensed_phase = 'reducedData'
f_pyrolsysis_exp = 'pyrolysisLengthExperiment'
f_burnout_exp = 'burnoutExp'

data_condensed_phase = np.loadtxt(f_condensed_phase)
data_pyrolysisExp = np.loadtxt(f_pyrolsysis_exp)
data_burnout_exp = np.loadtxt(f_burnout_exp)

plt.plot(data_condensed_phase[:,0]/60, data_condensed_phase[:,3], linestyle = '--', label = 'pyrolysis front simulation')
plt.plot(data_condensed_phase[:,0]/60, data_condensed_phase[:,6], linestyle = '--', label = 'burnout front simulation')
plt.xlim([0,125])
plt.ylim([0,4])
# plt.title('Pyrolysis Position')

plt.plot(data_burnout_exp[:,0]/60-data_burnout_exp[0,0]/60, data_burnout_exp[:,1], label = 'burnout front exp')
plt.plot(data_pyrolysisExp[:,0]/60-data_pyrolysisExp[0,0]/60, data_pyrolysisExp[:,1], label = 'pyrolysis front exp')

plt.xlabel('Time (min)')
plt.ylabel('Lengtn (m)')

plt.legend(loc = 'lower right')


