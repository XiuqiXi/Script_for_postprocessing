# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:34:56 2022

@author: cege
"""

import numpy as np

def extact_data_from_two_columns(file_1, file_2):
    file_1_data = np.loadtxt(file_1)
    file_2_data = np.loadtxt(file_2)
    
    extacted_data = np.zeros(shape=(len(file_2_data),1))
    
    for shortI, shortValue in enumerate(file_2_data[:,0]):
        for longI, longValue in enumerate(file_1_data[shortI:-1,0]):
            if abs(shortValue-longValue)<0.1:
                extacted_data[shortI] = file_1_data[longI,1]
                print(len(file_2_data)-shortI)
                break