import pysinewave
import random
import time
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Function to generate a random frequency logarithmically between 100 and 1000 Hz
def generate_random_frequency():
    min_frequency = 110
    max_frequency = 880
    num_frequencies = 36+1  # Increase this number for more frequency choices

    # Generate logarithmically spaced frequencies between min_frequency and max_frequency
    frequencies = np.logspace(np.log10(min_frequency), np.log10(max_frequency), num=num_frequencies)

    # Choose a random frequency from the generated frequencies
    return random.choice(frequencies)

def play_tone(frequency, sinewave, duration_ms):

    sinewave.set_frequency(frequency=frequency)
    # sinewave.set_pitch(pitch=frequency)
    time.sleep(0.3)


def calculate_score(actual_freq, guess_freq):
    # Calculate the pitch difference in semitones between the actual and guessed frequencies
    pitch_diff = pitch_difference(actual_freq, guess_freq)

    # Map the pitch difference to a score between 0 and 1000
    # In this example, we're using a linear mapping, but you can adjust it as needed
    # Smaller pitch_diff will result in a higher score, and vice versa
    max_pitch_diff = 12.0  # Maximum pitch difference in semitones (1 octave)
    score = max(0, int(1000 * (1 - abs(pitch_diff) / max_pitch_diff)))

    return score


def frequency_to_pitch(frequency):
    # The pitch notation consists of a letter representing the note (A, B, C, etc.)
    # and a number representing the octave (4, 5, 6, etc.)
    # The formula for converting frequency to pitch is:
    # pitch = 69 + 12 * log2(frequency / 440)
    # where 440 Hz is the frequency of A4 (the A above middle C)

    # Calculate the pitch using the formula
    pitch = 69 + 12 * np.log2(frequency / 440)

    # Define the notes and their corresponding names
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # Get the note and octave from the pitch value
    note_index = int(round(pitch)) % 12
    octave = int((pitch + 9) // 12)

    # Create the pitch notation (e.g., A4, C5, G#3, etc.)
    pitch_notation = f"{notes[note_index]}{octave}"

    return pitch_notation

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

def pitch_difference(frequency1, frequency2):
    # Calculate the pitch in semitones
    pitch1 = 69 + 12 * np.log2(frequency1 / 440)
    pitch2 = 69 + 12 * np.log2(frequency2 / 440)
    semitones_difference = pitch2 - pitch1

    return semitones_difference

def get_user_input():
    while True:
        user_input = input("Enter your guess for the frequency in Hz: ")
        try:
            guess_freq = float(user_input)
            if guess_freq <= 0:
                raise ValueError
            return guess_freq
        except ValueError:
            print("Invalid input! Please enter a positive number.")


class FrequencyGuessingGame:
    def __init__(self):
        self.max_rounds = 10
        self.current_round = 0
        self.score = 0
        self.actual_frequency = 0
        self.sinewave = pysinewave.SineWave(pitch=self.actual_frequency, pitch_per_second=300)
        self.sinewave.play()

        self.root = tk.Tk()
        self.root.title("Frequency Guessing Game")
        self.create_widgets()
        self.start_new_round()

    def create_widgets(self):
        self.label_frequency = ttk.Label(self.root, text="Frequency:")
        self.label_frequency.pack()

        self.label_pitch = ttk.Label(self.root, text="Pitch:")
        self.label_pitch.pack()

        self.slider = ttk.Scale(self.root, from_=110, to=880, orient="horizontal", command=self.on_slider_change, length=300)
        self.slider.pack()

        self.submit_button = ttk.Button(self.root, text="Submit", command=self.submit_guess)
        self.submit_button.pack()

        self.label_score = ttk.Label(self.root, text="Score:")
        self.label_score.pack()

        self.label_slider_value = ttk.Label(self.root, text="")
        self.label_slider_value.pack()

    def on_slider_change(self, value):
        # Get the current slider value
        frequency = float(value)

        # Calculate the pitch for each valid frequency
        valid_frequencies = np.logspace(np.log10(110), np.log10(880), num=36 + 1)
        valid_pitches = [frequency_to_pitch(freq) for freq in valid_frequencies]

        # Find the closest pitch to the current frequency
        closest_pitch = min(valid_pitches, key=lambda pitch: abs(frequency - pitch_to_frequency(pitch)))

        # Set the slider value to the frequency of the closest pitch
        # self.slider.set(pitch_to_frequency(closest_pitch))

        # Update the frequency and pitch labels with the current slider value
        self.update_frequency_pitch_labels(self.slider.get())


    def update_frequency_pitch_labels(self, value):
        # Get the slider value (frequency) and update the labels accordingly
        frequency = float(value)
        pitch = frequency_to_pitch(frequency)

        self.label_frequency.config(text=f"Frequency: {frequency:.2f} Hz")
        self.label_pitch.config(text=f"Pitch: {pitch}")

    def start_new_round(self):
        self.current_round += 1
        self.actual_frequency = generate_random_frequency()
        self.actual_pitch = frequency_to_pitch(self.actual_frequency)

        # Play the tone for a short duration
        print(f"Round {self.current_round}: Listen to the tone.")
        # print(f"Round {current_round}/{max_rounds}: Listen to the tone at {actual_frequency:.2f} Hz ({frequency_to_pitch(actual_frequency)}).")

        play_tone(self.actual_frequency, self.sinewave, duration_ms=2000)

        # self.label_frequency.config(text=f"Frequency: {self.actual_frequency:.2f} Hz")
        # self.update_frequency_pitch_labels(self.slider.get())
        # self.label_pitch.config(text=f"Pitch: {self.actual_pitch}")

    def submit_guess(self):
        guess_freq = self.slider.get()

        # Calculate the pitch difference and score
        diff_in_semitones = pitch_difference(self.actual_frequency, guess_freq)
        round_score = calculate_score(self.actual_frequency, guess_freq)
        self.score += round_score

        self.label_score.config(text=f"Score: {self.score}")
        messagebox.showinfo("Result", f"Actual Frequency: {self.actual_frequency:.2f} Hz ({frequency_to_pitch(self.actual_frequency)})\nYour guess: {guess_freq:.2f} Hz ({frequency_to_pitch(guess_freq)})\nPitch Difference: {diff_in_semitones:.2f} semitones.")

        if self.current_round < self.max_rounds:
            self.start_new_round()
        else:
            self.end_game()

    def end_game(self):
        messagebox.showinfo("Game Over", f"Game Over! Your final score: {self.score} / {1000*self.max_rounds}")
        self.sinewave.stop()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

def main():
    game = FrequencyGuessingGame()
    game.run()

if __name__ == "__main__":
    main()
