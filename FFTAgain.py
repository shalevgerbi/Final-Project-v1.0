import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy import signal as mySignal

sampFreq, sound = wavfile.read('./DemoCDE.wav')
print(f"samefreq: {sampFreq}, sound: {sound}")
print(f"q: {2.0 ** 15}")
sound = sound / 2.0 ** 15
print("sound", sound)
print(f"shape: {sound.shape}")
# sound.shape = length of data
# sempfreq = how many freq per millisecond?
length_in_s = sound.shape[0] / sampFreq
print(length_in_s)
# lenght_in_s = lenght in seconds of wav file

print(f"arrange: {np.arange(sound.shape[0])}")  # works like range
print()
time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s
print(f"time: {time}")
plt.subplot(2, 1, 1)
plt.plot(time, sound[:, 0], 'r')
plt.xlabel("time, s [left channel]")
plt.ylabel("signal, relative units")
plt.subplot(2, 1, 2)
plt.plot(time, sound[:, 1], 'b')
plt.xlabel("time, s [right channel]")
plt.ylabel("signal, relative units")
plt.tight_layout()
plt.show()

signal = sound[:, 0]

fft_spectrum = np.fft.rfft(signal)
signalFilter = []
for i in signal:
    if i > 0.1 or i < -0.1:
        signalFilter.append(i)
print("signalFilter: ", signalFilter)
freq = np.fft.rfftfreq(signal.size, d=1. / sampFreq)
print("________")
print("fft spectrum")
print(fft_spectrum)
print("________")
fft_spectrum_abs = np.abs(fft_spectrum)
print("absolute fft spectrum")
print(fft_spectrum_abs)
#fft_spectrum_abs.np.fft.rfft
freqArr = []
di = dict()
for i, f in enumerate(fft_spectrum_abs):
    if f > 350:  # looking at amplitudes of the spikes higher than 350
        print('frequency = {} Hz with amplitude {} '.format(np.round(freq[i], 0), np.round(f)))
        if int(freq[i]) in di:
            di[int(freq[i])] += 1
        else:
            di[int(freq[i])] = 1

print(di)
knownFreq = [
    16.35,
    17.32,
    18.35,
    19.45,
    20.6,
    21.83,
    23.12,
    24.5,
    25.96,
    27.5,
    29.14,
    30.87,
    32.7,
    34.65,
    36.71,
    38.89,
    41.2,
    43.65,
    46.25,
    49,
    51.91,
    55,
    58., 27,
    61.74,
    65.41,
    69.3,
    73.42,
    77.78,
    82.41,
    87.31,
    92.5,
    98,
    103.83,
    110,
    116.54,
    123.47,
    130.81,
    138.59,
    146.83,
    155.56,
    164.81,
    174.61,
    185,
    196,
    207.65,
    220,
    233.08,
    246.94,
    261.63,
    277.18,
    293.66,
    311.13,
    329.63,
    349.23,
    369.99,
    392,
    415.3,
    440,
    466.16,
    493.88,
    523.25,
    554.37,
    587.33,
    622.25,
    659.25,
    698.46,
    739.99,
    783.99,
    830.61,
    880,
    932.33,
    987.77,
    1046.5,
    1108.73,
    1174.66,
    1244.51,
    1318.51,
    1396.91,
    1479.98,
    1567.98,
    1661.22,
    1760,
    1864.66,
    1975.53,
    2093,
    2217.46,
    2349.32,
    2489.02,
    2637.02,
    2793.83,
    2959.96,
    3135.96,
    3322.44,
    3520,
    3729.31,
    3951.07,
    4186.01,
    4434.92,
    4698.63,
    4978.03,
    5274.04,
    5587.65,
    5919.91,
    6271.93,
    6644.88,
    7040,
    7458.62,
    7902.13
]


temp = di.items()
print(temp)

finalDict = dict()

for key, value in di.items():
    for i in knownFreq:
        if i + 5 > key > i - 5:
            if i in finalDict:
                finalDict[i] += value
            else:
                finalDict[i] = value

# finalDict = {k: v for k, v in sorted(finalDict.items(), key=lambda item: item[1], reverse=True)}
sortedDict = {k: v for k, v in sorted(finalDict.items(), key=lambda item: item[1], reverse=True)}
# dict(sorted(finalDict.items(), key=lambda item: item[1]))
print(finalDict)
# maxVal = finalDict
print(list(finalDict.keys())[0])
keysArr = []
maxVal = (list(sortedDict.values())[0])

for key, value in finalDict.items():
    if value > maxVal / 2:
        keysArr.append(key)
print(keysArr)

for i, f in enumerate(freq):
    if f < 62 and f > 58:  # (1)
        fft_spectrum[i] = 0.0
    if f < 21 or f > 20000:  # (2)
        fft_spectrum[i] = 0.0

plt.plot(freq[:3000], np.abs(fft_spectrum[:3000]))
plt.xlabel("frequency, Hz")
plt.ylabel("Amplitude, units")
plt.show()

plt.plot(np.abs(fft_spectrum_abs[:88200]), time[:176400:2])
plt.ylabel("frequency, Hz")
plt.xlabel("Time")
plt.show()


#plt.plot(np.abs(fft_spectrum_abs[:3150]), time[:176400:56])
plt.ylabel("frequency, Hz")
plt.xlabel("Time")

plt.plot(time[::2], fft_spectrum_abs[:-1], 'r')
plt.show()
# x = myFft.fft(sound);
# print("x: ",x)
# plt.plot(x,0), fft_spectrum_abs[:-1], 'r')
# plt.show()

rng = np.random.default_rng()
fs = 44100
N = 176400
amp = 2 * np.sqrt(2)
noise_power = 0.01 * fs / 2

#noise_power = 0
time = np.arange(N/2 +1) / float(fs)
mod = 500*np.cos(2*np.pi*0.25*time)
mod = fft_spectrum_abs
carrier = amp * np.sin(2*np.pi*3e3*time + mod)
carrier = signal[:88201]
noise = rng.normal(scale=np.sqrt(noise_power),
                   size=time.shape)
noise *= np.exp(-time/5)
x = carrier + noise
f, t, Zxx = mySignal.stft(x, fs, nperseg=1000)
plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp, shading='gouraud')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()


# frequencies, times, spectrogram = signal.spectrogram(samples, sampFreq)



# plt.pcolormesh(times, frequencies, spectrogram)
# #plt.imshow(spectrogram)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()



