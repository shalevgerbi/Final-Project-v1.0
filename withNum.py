import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io import wavfile

sample_rate, samples = wavfile.read('Mary-Had.wav')

frequencies, times, spectrogram = signal.spectrogram(samples[:,1], sample_rate)
# frequencies2, times2, spectrogram2 = signal.spectrogram(samples[:,1], sample_rate)
print("sampleRate", sample_rate)
print("samples", samples)

ax = plt.gca()
ax.set_xlim([0, 15])
ax.set_ylim([250, 1000])
finalFreq = []
# finalSpec = []
# for i in range(len(frequencies)):
#     finalFreq.append(np.maximum(frequencies[i], frequencies2[i]))
#     # spectrogram

print("frequencies",frequencies)
print("spectogram",spectrogram)
plt.pcolormesh(times, frequencies, spectrogram/2)
# plt.imshow(spectrogram)
plt.yticks(range(0, 1000,50))
# plt.x(times)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()


ax = plt.gca()
ax.set_xlim([0, 4])
ax.set_ylim([250, 1000])
# plt.pcolormesh(times2, frequencies2, spectrogram2)
# plt.imshow(spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()