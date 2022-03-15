from signal import signal

import numpy as np
import scipy.signal
from scipy import fft
from scipy.io import wavfile

samplerate, data = wavfile.read('./demo.wav')
# print(samplerate, data)
nums = fft.fft(data)
freq = scipy.fft.fftfreq(nums)
# print(nums)
# print(freq)


fft_spectrum = np.fft.rfft(signal)
freq = np.fft.rfftfreq(signal.size, d=1./samplerate)

print(freq)
# for note in data:
#     print(note * 44100 / 1024)
