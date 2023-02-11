# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 14:53:20 2023

@author: xxi1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import interpolate
import math
from matplotlib import cm

global domainSize1
global domainSize2

def readFiles():
    
    global domainSize1
    global domainSize2
    
    df = pd.read_csv('slice.csv')
    
    unit = df.iloc[0]
    
    df = df.iloc[1:-1]
    
    id = df.columns.values.tolist()
    
    x = np.asfarray(df[id[0]].values)
    domainSize1 = len(x)
    y = np.asfarray(df[id[1]].values)
    domainSize2 = len(y)
    
       
    xll = float(min(x))
    xul = float(max(x))
    yll = float(min(y))
    yul = float(max(y))

    for i in range(2,len(id)):
        z = np.asfarray(df[id[i]].values)
        zll = float(min(z))
        zul = float(max(z))
        plot_contour(x,y,z,xll,xul,yll,yul,zll,zul,id[i])


def plot_contour(Coordx,Coordy,sliceData,minX,maxX,minY,maxY,minZ,maxZ,sliceName):

    global domainSize1
    global domainSize2    

    X = np.linspace(minX, maxX, 200)
    Y = np.linspace(minY, maxY, 200)

    X1, Y1 = np.meshgrid(X, Y)

    Z = interpolate.griddata((Coordx, Coordy), sliceData, (X1, Y1), method='cubic')
  
    fig, ax = plt.subplots(figsize=(12, 12*domainSize1/domainSize2))


    levels = np.linspace(minZ,maxZ,100) 
    cset1 = ax.contourf(X1, Y1, Z, levels,cmap=cm.jet, extend='max') 


    ax.set_title(sliceName,size=20)

    ax.set_xlim(minX, maxX)
    ax.set_ylim(minY, maxY)
    ax.set_xlabel("X(m)",size=15)
    ax.set_ylabel("Y(m)",size=15)


    cbar = fig.colorbar(cset1)
    cbar.set_label(sliceName, size=18)
    cbar.set_ticks([minZ, maxZ])
   
   
    # fig.savefig(figName+".png", bbox_inches='tight',dpi=150,pad_inches=0.1)
    plt.show()
 
    return()

if __name__ == '__main__':
    readFiles()
