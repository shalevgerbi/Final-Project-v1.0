from math import sqrt

import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from scipy.io import wavfile
N = 1024 # size of FFT and sample window
Fs = 44100  # sample rate = 44.1 kHz
data = [None] * N  # input PCM data buffer
fft = [None] * N * 2
NDiv = int(N / 2)
# FFT complex buffer (interleaved real/imag)
magnitude = [None] * NDiv  # power spectrum

# // capture audio in data[] buffer
# // ...
Fs, prevData = wavfile.read('./demo.wav')
for i in range(0, len(prevData[1])):
    data.append(prevData[1][i])
# // apply window function to data[]
# // ...

# middleArr =[]
# for r in range(0, len(data)):
#     for c in range(0, len(data[r])):
#         middle = data[r][c]
#         middleArr.append(middle)


# // copy real input data to complex FFT buffer
for i in range(0, N - 1):
    fft[2 * i] = data[i]
    fft[2 * i + 1] = 0

# // perform in-place complex-to-complex FFT on fft[] buffer
# // ...

# // calculate power spectrum (magnitude) values from fft[]
for i in range(0, N-1):
    re = fft[2 * i]
    im = fft[2 * i + 1]
    if re is not None and re > 0 and im > 0 and im is not None:
        magnitude[i] = sqrt(re * re + im * im)

# // find largest peak in power spectrum
max_magnitude = -99999999
max_index = -1
for i in range(0, int(N / 2 - 1)):
    if magnitude[i] is not None:
        if magnitude[i] > max_magnitude:
            max_magnitude = magnitude[i]
            max_index = i

# // convert index of largest peak to frequency
freq = max_index * Fs / N

print(freq)
