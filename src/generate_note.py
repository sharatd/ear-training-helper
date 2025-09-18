import numpy as np
import sounddevice as sd

# Parameters
sample_rate = 44100   # sample rate (samples per second)
duration = 1.0  # seconds

# Time array
# int(sample_rate * duration) gives us # of samples so this linspace function is gonna return
# the times at which we're taking a total of 44,100 samples over duration (1 second)
# Therefore, it'll be an array of 44,100 times
time_array = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
print("The first 10 elements of time_array when endpoint set to False:", time_array[:10])
print("The last 10 elements of time_array when endpoint set to False:", time_array[-10:])

# Time array where endpoint is set to True
time_array_2 = np.linspace(0, duration, int(sample_rate * duration), endpoint=True)
print("The first 10 elements of time_array_2 when endpoint set to True:", time_array_2[:10])
print("The last 10 elements of time_array_2 when endpoint set to True:", time_array_2[-10:])

# Create sine wave array for given frequency
freq = 440  # A4
sin_wave_array = np.sin(time_array * freq * 2 * np.pi)


# Play sine wave
sd.play(sin_wave_array, sample_rate)
sd.wait()