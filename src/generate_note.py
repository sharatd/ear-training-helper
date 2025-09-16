import numpy as np

# Parameters
sample_rate = 44100   # sample rate (samples per second)
duration = 1.0  # seconds

# Time array
time_array = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
# int(sample_rate * duration) gives us # of samples so this linspace function is gonna return
# the times at which we're taking a total of 44,100 samples over duration (1 second)
# Therefore, it'll be an array of 44,100 times

# Create sine wave array for given frequency
freq = 440  # A4
sin_wave_array = np.sin(time_array * freq * 2 * np.pi)