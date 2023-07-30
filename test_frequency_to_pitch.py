import unittest
import numpy as np
# from gui import frequency_to_pitch

def frequency_to_pitch(frequency):
    # The pitch notation consists of a letter representing the note (A, B, C, etc.)
    # and a number representing the octave (0, 1, 2, etc.).
    # The formula for converting frequency to pitch is:
    # pitch = 69 + 12 * log2(frequency / 440)
    # where 440 Hz is the frequency of A4 (the A above middle C).

    # Calculate the pitch using the formula
    pitch = 69 + 12 * np.log2(frequency / 440)

    # Round the pitch to the nearest whole number to get the index of the note
    note_index = round(pitch) % 12

    # Get the octave from the pitch value
    octave = int((pitch - 11.5) // 12)  # Adjusting the octave numbering

    # Define the notes and their corresponding names
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # Create the pitch notation (e.g., A4, C5, G#3, etc.)
    pitch_notation = f"{notes[note_index]}{octave}"

    return pitch_notation


class TestFrequencyToPitch(unittest.TestCase):
    def test_frequency_to_pitch(self):
        test_cases = [
            # (frequency, expected_pitch)
            (27.5, "A0"),
            (110, "A2"),
            (261.63, "C4"),
            (440, "A4"),
            (523.25, "C5"),
            (880, "A5"),
            (4186.01, "C8"),
        ]

        for frequency, expected_pitch in test_cases:
            with self.subTest(frequency=frequency, expected_pitch=expected_pitch):
                actual_pitch = frequency_to_pitch(frequency)
                self.assertEqual(actual_pitch, expected_pitch)

if __name__ == "__main__":
    unittest.main()