# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:56:24 2021

@author: cege
"""

import cv2 as cv
import numpy as np
from Hibert import mapping

color_bar = cv.imread('Fcolor_bar.png')
figure = cv.imread('figure.png')

color_bar[:, :, 1] = 0
figure[:, :, 1] = 0

cv.imshow('figure', figure)
cv.imshow('color_bar', color_bar)

lin_color_bar = color_bar[:, int(9/2),:]

height = figure.shape[0]
length = figure.shape[1]

Hilbert_line = mapping(length, height)

figure = figure[:, :, [0, 2]]
lin_color_bar = lin_color_bar[: ,[0, 2]]

Hilbert_line_figure = np.zeros([len(Hilbert_line), 2])

i = 0
for y in range(height):
    for x in range(length):
        Hilbert_line_figure[i, 0] = figure[y, x, 0]
        Hilbert_line_figure[i, 1] = figure[y, x, 1]
        i = i+1
        
mappings = np.zeros([len(Hilbert_line), 1])
for i in range(len(Hilbert_line_figure)):
    for j in range(len(lin_color_bar)):
        if Hilbert_line_figure[i, 0] == lin_color_bar[j, 0] and Hilbert_line_figure[i, 1] == lin_color_bar[j, 1]:
            mappings[i] = j
            print(i)
            break

data = np.zeros([height, length])
for i in range(len(mappings)):
    data[Hilbert_line[i, 1], Hilbert_line[i, 0]] = mappings[i]

# # Step1. 加载图像
# img = figure

# # Step2. 创建掩模、背景图和前景图
# mask = np.zeros(img.shape[:2], np.uint8)# 创建大小相同的掩模
# bgdModel = np.zeros((1,65), np.float64)# 创建背景图像
# fgdModel = np.zeros((1,65), np.float64)# 创建前景图像

# # Step3. 初始化矩形区域
# # 这个矩形必须完全包含前景
# rect = (50,0,length, height) #格式为（x, y, w, h）

# # Step4. GrubCut算法，迭代5次
# # mask的取值为0,1,2,3
# cv.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT) # 迭代5次

# # Step5. mask中，值为2和0的统一转化为0, 1和3转化为1
# mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
# img = img * mask2[:,:,np.newaxis] # np.newaxis 插入一个新维度，相当于将二维矩阵扩充为三维

# cv.imshow('figure', figure)

# data = np.zeros([height, length])

# for y in range(height):
#     for x in range(length):
#         print(str(x) + ',' + str(y))
#         for color_index in range(len(lin_color_bar)):
#             if np.linalg.norm(figure[y, x, :] - lin_color_bar[color_index, :])<5:
#                 data[y, x] = color_index
#                 break