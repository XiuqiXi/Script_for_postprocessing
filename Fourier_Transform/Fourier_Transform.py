
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 23:06:33 2022

@author: Tingyou
"""


import statsmodels.tsa.api as smt
import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as plt
from scipy import signal
import scipy.io.wavfile as wf
# Import math Library
import math


data = np.loadtxt('Draft1.txt', delimiter = '\t')



time = data[:,0] #Draft1
measuredSignal = data[:,1]

# print(sample_rate, noised_signs.shape)  # 采样率 (每秒个数), 采样位移
# noised_signs = noised_signs / (2 ** 15)
# measuredSignal = noised_signs
# time = np.arange(noised_signs.size) / sample_rate  # x轴

####################################################

sample_rate = int(1/(time[10]-time[9]))
#sample_rate=1e9;

plt.figure("Filter", facecolor="lightgray")
plt.subplot(221)
plt.title("Time Domain", fontsize=12)
plt.ylabel("Signal", fontsize=12)
plt.grid(linestyle=":")
plt.plot(time, measuredSignal, color="b", label="Noised")
plt.legend()
plt.tight_layout()

# FFT transformation

complex_ary = nf.fft(measuredSignal)

fft_freqs = nf.fftfreq(measuredSignal.size, d=sample_rate**(-1))  # Frequency series
fft_pows = np.abs(complex_ary)

plt.subplot(222)
plt.title("Frequency", fontsize=12)
plt.ylabel("pow", fontsize=12)
plt.grid(linestyle=":")
plt.semilogy(fft_freqs[fft_freqs > 0], fft_pows[fft_freqs > 0], color="orangered", label="Noised")
plt.legend()
plt.tight_layout()
plt.xlim([0,100000000])

#Reduce noise
fund_freq = fft_freqs[fft_pows.argmax()]
# fund_freq=-5.75e7

noised_indices = np.where(fft_freqs != fund_freq)
filter_fft = complex_ary.copy()
filter_fft[noised_indices] = 0  # 噪声数据位置 =0
filter_pow = np.abs(filter_fft) 

plt.subplot(224)
plt.title("Filter Frequency ", fontsize=12)
plt.ylabel("pow", fontsize=12)
plt.grid(linestyle=":")
plt.semilogy(fft_freqs[fft_freqs > 0], filter_pow[fft_freqs > 0], color="orangered", label="Filter")
plt.legend()
plt.tight_layout()

#Inverse FT
filter_sign = nf.ifft(filter_pow).real

plt.subplot(223)
plt.title("Filter Time Domain", fontsize=12)
plt.ylabel("filter_signal", fontsize=12)
plt.grid(linestyle=":")
plt.plot(time, filter_sign, color="b", label="Filter")
plt.legend()
plt.tight_layout()

