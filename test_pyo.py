# pip install pyo
from pyo import *
import time

try:
    # Initialize the Pyo server
    s = Server().boot().start()

    # Create a sine wave oscillator
    freq = 440  # Frequency in Hz (A4 note)
    amp = 0.5   # Amplitude (0 to 1)
    oscillator = Sine(freq=freq, mul=amp)

    print("Start playout")

    # Start the oscillator
    oscillator.out()

    # Sleep for a short duration to hear the sound
    time.sleep(2)

    print("Ending Playout")

    # Stop the server
    s.shutdown()

except Exception as e:
    print(f"An error occurred: {e}")
