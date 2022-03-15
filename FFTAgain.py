import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)
sampFreq, sound = wavfile.read('./DemoD.wav')

print(sound.dtype, sampFreq)

sound = sound / 2.0**15
print(sound.shape)

length_in_s = sound.shape[0] / sampFreq
print(length_in_s)

# plt.subplot(2,1,1)
# plt.plot(sound[:,0], 'r')
# plt.xlabel("left channel, sample #")
# plt.subplot(2,1,2)
# plt.plot(sound[:,1], 'b')
# plt.xlabel("right channel, sample #")
# plt.tight_layout()
# plt.show()

time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s

# plt.subplot(2,1,1)
# plt.plot(time, sound[:,0], 'r')
# plt.xlabel("time, s [left channel]")
# plt.ylabel("signal, relative units")
# plt.subplot(2,1,2)
# plt.plot(time, sound[:,1], 'b')
# plt.xlabel("time, s [right channel]")
# plt.ylabel("signal, relative units")
# plt.tight_layout()
# plt.show()

signal = sound[:,0]

# plt.plot(time[6000:7000], signal[6000:7000])
# plt.xlabel("time, s")
# plt.ylabel("Signal, relative units")
# plt.show()

fft_spectrum = np.fft.rfft(signal)
freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)

print(fft_spectrum)

fft_spectrum_abs = np.abs(fft_spectrum)
#
# plt.plot(freq, fft_spectrum_abs)
# plt.xlabel("frequency, Hz")
# plt.ylabel("Amplitude, units")
# plt.show()

# plt.plot(freq[:500], fft_spectrum_abs[:500])
# plt.xlabel("frequency, Hz")
# plt.ylabel("Amplitude, units")
# plt.arrow(90, 5500, -20, 1000, width=2, head_width=8, head_length=200, fc='k', ec='k')
# plt.arrow(200, 4000, 20, -1000, width=2, head_width=8, head_length=200, fc='g', ec='g')
# plt.show()




freqArr = []
di = dict()
for i,f in enumerate(fft_spectrum_abs):
    if f > 350: #looking at amplitudes of the spikes higher than 350
        print('frequency = {} Hz with amplitude {} '.format(np.round(freq[i],0),  np.round(f)))
        if int(freq[i]) in di:
            di[int(freq[i])] += 1
        else:
            di[int(freq[i])] = 1

print(di)
knownFreq =[
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
58.,27,
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
        if i+5 > key > i-5:
            if i in finalDict:
                finalDict[i] += value
            else:
                finalDict[i] = value


finalDict = {k: v for k, v in sorted(finalDict.items(), key=lambda item: item[1], reverse=True)}
# dict(sorted(finalDict.items(), key=lambda item: item[1]))
print(finalDict)
# maxVal = finalDict
print(list(finalDict.keys())[0])


# for num in knownFreq:
#     for key, value in di.items():
#         if (num + 5) > key > (num - 5):
#             if finalDict is None:
#
#                 finalDict[key] = value
#                 continue
#             finalDict[key] = value



        # if(freqArr.int(freq[i]))
        # freqArr.append(int(freq[i]))

# for i in range(0,len(di)):
#

# x = map
# counter=[]
# freq = []
# for i,f in enumerate(fft_spectrum_abs):
#     if f > 350:  # looking at amplitudes of the spikes higher than 350
#          freq.append(np.round(freq[i],0))
#
# notes = dict
#
# for i, f in enumerate(fft_spectrum_abs):
#     if f > 350:  # looking at amplitudes of the spikes higher than 350
#
#         if int(np.round(freq[i])) in notes:
#             notes[int(np.round(freq[i]))] += 1
#         else:
#             notes[int(np.round(freq[i]))] = 1
#
#
#

