import unittest

def pitch_to_frequency(pitch):
    # The pitch notation consists of a letter representing the note (A, B, C, etc.)
    # and a number representing the octave (4, 5, 6, etc.)
    # The formula for converting pitch to frequency is the reverse of the frequency_to_pitch formula:
    # frequency = 440 * 2 ** ((pitch - 69) / 12)
    # where 440 Hz is the frequency of A4 (the A above middle C)

    # Split the pitch notation into the note and octave parts
    note, octave = pitch[:-1], int(pitch[-1])

    # Define the notes and their corresponding indices
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note_index = notes.index(note)

    # Calculate the pitch value using the formula
    pitch_value = (octave + 1) * 12 + note_index

    # Calculate the frequency using the reverse formula
    frequency = 440 * 2 ** ((pitch_value - 69) / 12)

    return frequency

class TestPitchToFrequency(unittest.TestCase):

    def test_pitch_to_frequency(self):
        # Test cases with pitch notations and their corresponding frequencies
        test_cases = [
            ("A4", 440.0),
            ("C#5", 554.3652619537443),
            ("G#3", 207.65234878997256),
            ("F4", 349.2282314330039),
            ("D#6", 1244.5079348883237),
        ]

        for pitch, expected_frequency in test_cases:
            with self.subTest(pitch=pitch):
                frequency = pitch_to_frequency(pitch)
                self.assertAlmostEqual(frequency, expected_frequency, places=5)

if __name__ == "__main__":
    unittest.main()