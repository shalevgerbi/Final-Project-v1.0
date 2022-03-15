import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()
from scipy.signal import get_window

m = 513
t = np.arange(m)

w = get_window('hamming', m)

plt.plot(t, w)
plt.xlabel("(time) sample #")
plt.ylabel("amplitude")
plt.title("hamming window")
plt.xlim(0, m-1)
plt.ylim(-0.025, 1.025)
plt.show()

w_fft = np.fft.rfft(w)

freqs = np.fft.rfftfreq(w.size, d=1/m)

plt.plot(freqs, np.abs(w_fft))
plt.show()

plt.plot(freqs, np.abs(w_fft))
plt.xlim(0, 20)
plt.show()

n = 4096
w_fft = np.fft.rfft(w, n=4096)
freqs = np.fft.rfftfreq(n, d=1/m)
plt.plot(freqs, np.abs(w_fft))
plt.xlim(0, 20)

plt.plot(freqs, 20*np.log10(np.abs(w_fft) / np.abs(w_fft).max()))
plt.xlim(0, 20)

plt.show()


def compute_mainlobe_width(spectrum):
    """
    computes mainlobe width from spectrum

    assumes the mainlobe starts at 0, that spectrum size is odd, and that
    the spectrum is real-valued (half of the frequencies)

    returns the number of samples of full mainlobe (not just half)
    """
    abs_spectrum = np.abs(spectrum)
    current_value = abs_spectrum[0]
    for ind, next_value in enumerate(abs_spectrum):
        if next_value > current_value:
            break
        else:
            current_value = next_value
    return 2 * ind - 1


compute_mainlobe_width(w_fft)

np.abs(w_fft)[:17]

np.abs(w_fft)[17]


def compute_sidelobe_level(spectrum):
    """
    computes sidelobe level from spectrum

    assumes the mainlobe starts at 0, that spectrum size is odd, and that
    the spectrum is real-valued (half of the frequencies)

    returns the level of sidelobes in dB
    """
    mainlobe_width = compute_mainlobe_width(spectrum)

    ind = (mainlobe_width - 1) / 2

    abs_spectrum = np.abs(spectrum)

    return 20 * np.log10(abs_spectrum[ind:].max() / abs_spectrum.max())

plt.plot(freqs, 20*np.log10(np.abs(w_fft) / np.abs(w_fft).max()))
plt.xlim(0, 20)
width = compute_mainlobe_width(w_fft)
level = compute_sidelobe_level(w_fft)

ylim_range = plt.ylim()
plt.vlines((width - 1) / 2 * m / n, ylim_range[0], ylim_range[1], lw=3)
xlim_range = plt.xlim()
plt.hlines(level, xlim_range[0], xlim_range[1], lw=3)

plt.show()


for window in ['boxcar', 'hanning', 'hamming', 'blackman', 'blackmanharris']:
    m = 513
    w = get_window(window, m)
    n = 4096
    w_fft = np.fft.rfft(w, n)
    freqs = np.fft.rfftfreq(n, d=1/m)
    plt.figure(figsize=(10, 4))
    plt.subplot(121)
    plt.plot(t, w)
    plt.xlabel("sample #")
    plt.ylabel("amplitude")
    plt.title("{} window".format(window))
    plt.xlim(0, t.size)
    plt.ylim(-0.025, 1.025)
    plt.subplot(122)
    plt.plot(freqs, 20*np.log10(np.abs(w_fft) / np.abs(w_fft).max()))
    plt.xlim(0, 25)
    plt.ylim(-120, 1)
    width = compute_mainlobe_width(w_fft)
    width_bins = width * m / n
    level = compute_sidelobe_level(w_fft)
    ylim_range = plt.ylim()
    plt.vlines((width - 1) / 2 * m / n, ylim_range[0], ylim_range[1], lw=3)
    xlim_range = plt.xlim()
    plt.hlines(level, xlim_range[0], xlim_range[1], lw=3)
    plt.title("{} window\nmainlobe width = {:.0f} bins, sidelobe level = {:.0f} dB".format(window,
                                                                       width_bins,
                                                                       level))
    plt.xlabel('frequency bin #')
# note c is 261.626 hz
sr = 48000
bl = 150
fn = sr / 2
print("fn: ",fn)
d = bl / sr
print("d: ",d)
df = sr/bl
print("df: ",df)



print(len('jdbc:derby:C:\\Users\\shalev\\Desktop\\java_temp\\ForTest2022_SecondTry\\my_db'))
time = 1;
freq = 220500;
