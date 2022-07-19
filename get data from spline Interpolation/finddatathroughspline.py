# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 17:34:33 2022

@author: cege
"""

import numpy as np
import numpy as np, matplotlib.pyplot as plt
from scipy.interpolate import interp1d



splinedata = np.loadtxt('splineData.txt')

inputdataX = np.loadtxt('inputDataX.txt')

x = splinedata[:,0]
y = splinedata[:,1]

f = interp1d(x, y, kind = 'cubic')

outputdataY = f(inputdataX)

plt.plot(x,y)
plt.plot(inputdataX, outputdataY)

