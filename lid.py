import numpy as np
import sounddevice as sd
from pybooklid import LidSensor

fs = 44100
duration = 0.5
volume = 0.5

def play_tone(freq):
    t = np.linspace(0, duration, int(fs * duration), False)
    tone = np.sin(freq * 2 * np.pi * t) * volume
    sd.play(tone, fs)


with LidSensor() as sensor:
        for angle in sensor.monitor(interval=0.1):
            play_tone(angle*10)
            print(f"Playing note at : {angle*10} Hz")
            if angle < 5:  # Nearly closed
                break

