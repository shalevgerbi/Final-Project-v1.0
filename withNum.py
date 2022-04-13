import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io import wavfile

sample_rate, samples = wavfile.read('DemoCDE.wav')


frequencies, times, spectrogram = signal.spectrogram(samples[:, 1], sample_rate)
# frequencies2, times2, spectrogram2 = signal.spectrogram(samples[:,1], sample_rate)
print("sampleRate", sample_rate)
print("samples", samples)
# plt.rcParams["figure.figsize"] = (14, 8)

ax = plt.gca()
ax.set_xlim([0, 15])
ax.set_ylim([250, 1000])
# Pxx, freqs, bins, im = ax.specgram(samples[:, 1],NFFT=1024,Fs=sample_rate, noverlap=512)
finalFreq = []
# finalSpec = []
# for i in range(len(frequencies)):
#     finalFreq.append(np.maximum(frequencies[i], frequencies2[i]))
#     # spectrogram

print("frequencies",frequencies)
print("spectogram",spectrogram)


plt.pcolormesh(times, frequencies, spectrogram)
# plt.imshow(spectrogram)
plt.yticks(range(0, 1000,50))
# plt.x(times)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.xlim([0,4])
plt.show()


ax = plt.gca()
ax.set_xlim([0, 4])
ax.set_ylim([250, 1000])
# plt.pcolormesh(times2, frequencies2, spectrogram2)
# plt.imshow(spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

