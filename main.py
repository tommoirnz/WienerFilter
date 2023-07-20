import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import wiener, lfilter

# Parameters
N = 200  # Number of samples
fs = 1    # Sampling frequency

# Generate white noise
white_noise = np.random.normal(0, 1, N)

# Generate colored noise by passing white noise through a second-order system
b = [1]  # Numerator coefficients
a = [1, -1, 0.5]  # Denominator coefficients
colored_noise = lfilter(b, a, white_noise)

# Add additive white noise
noise_power = 0.5  # Power of the additive white noise
additive_noise = np.random.normal(0, np.sqrt(noise_power), N)
signal = colored_noise + additive_noise

# Apply Wiener filter to estimate the colored noise signal
filtered_signal = wiener(signal, mysize=5)

# Plot the random signal and its estimate
time = np.arange(N) / fs
plt.figure()
plt.plot(time, signal, label='Random Signal')
plt.plot(time, filtered_signal, label='Filtered Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

