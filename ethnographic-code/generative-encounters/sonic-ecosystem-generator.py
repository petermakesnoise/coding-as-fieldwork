"""
Sonic Ecosystem Generator
This script generates a layered ambient soundscape using PyDub, simulating a
virtual acoustic ecology. Each layer represents a 'species' or 'force' in the system.
"""

from pydub.generators import Sine
from pydub import AudioSegment

# Frequencies as symbolic species
species = {
    "crickets": 5000,
    "wind": 440,
    "drone": 110,
}

duration_ms = 10000  # 10 seconds

layers = []
for name, freq in species.items():
    tone = Sine(freq).to_audio_segment(duration=duration_ms).apply_gain(-20)
    print(f"Generated: {name} at {freq}Hz")
    layers.append(tone)

soundscape = sum(layers)
soundscape.export("sonic_ecosystem.wav", format="wav")
print("Exported sonic_ecosystem.wav")
