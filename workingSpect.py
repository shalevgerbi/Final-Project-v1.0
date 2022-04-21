import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io import wavfile


# reading audio (.wav) file
# sample_rate, samples = wavfile.read('DemoD.wav')

sample_rate, samples = wavfile.read('doremi.wav')
# sample_rate, samples = wavfile.read('DemoCDEFD#G#.wav')
# sample_rate, samples = wavfile.read('DemoCDEFD#G#Octave.wav')
# sample_rate, samples = wavfile.read('DemoCDEFD#G#MONO.wav')
# converts signal into frequency, time, and [frequency,time] amplitude with resolution of 2**12
# resolution needs to be high but not more than length of signal
##f, t, Sxx = signal.spectrogram(samples[:,0],sample_rate,nperseg=4096*2)
f, t, Sxx = signal.spectrogram(samples[:,0], sample_rate  ,nperseg=sample_rate)
# f2, t2, Sxx2 = signal.spectrogram(samples[:,1], sample_rate, nperseg=44100//4)
# f2, t2, Sxx = signal.spectrogram(samples[:,1], sample_rate, nperseg=44100//8)
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

arr = []

#finding max col in Sxx
xmax = Sxx.max(axis=0)
# xmax2 = Sxx2.max(axis=0)
# Sxx.index(xmax[0])


#append to indexArr the indexes of the max value in Sxx
# for i in range(len(xmax)):
#     indexArr.append(np.where(Sxx == xmax[i]))
# print(xmax)
# print(indexArr)


indexArr = []
indexArr2 =[]
# indexArr.append(np.argmax(Sxx,axis=0) *4 )
indexArr2.append(np.argmax(Sxx,axis=0))
print("indexArr",indexArr)
print("indexArr2",indexArr2)

maxArr=[]
# for i in range(len(indexArr)):
    # if np.any(Sxx[indexArr[i]][i] > Sxx2[indexArr2[i]][i]):
    #     maxArr.append(indexArr[i])
    # else:
    #     maxArr.append(indexArr2[i])
    # maxArr.append(np.maximum(Sxx[indexArr[i],i] * 8,Sxx2[indexArr2[i],i] * 8))

print("maxArr", maxArr)

# for i in range(len(Sxx)):
#     arr.append(max(Sxx[:,i]))
# print(arr)

finalDict = dict
finalArr = []
for item in indexArr2[0]:
    for i in range(len(knownFreq)-1):
        if knownFreq[i] + 6 > item > knownFreq[i] - 6:
            first_freq = abs(knownFreq[i] - item)
            second_freq = abs(knownFreq[i+1] - item)
            if min(first_freq,second_freq) == first_freq:
                finalArr.append(knownFreq[i])
            else:
                finalArr.append(knownFreq[i+1])

print(finalArr)
# plot the graph
ax = plt.gca()
highestFreq = 1000  # 1000 may be too low if we have higher notes
ax.set_ylim([0, highestFreq])
plt.yticks(range(0, highestFreq, 50))
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()