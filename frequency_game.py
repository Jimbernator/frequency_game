#!/usr/bin/python
import pysinewave
import pygame
import random
import time
import numpy as np


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


def main():
    max_rounds = 10
    current_round = 0
    score = 0
    actual_frequency = 0
    sinewave = pysinewave.SineWave(pitch = actual_frequency, pitch_per_second=300)
    sinewave.play()

    while current_round < max_rounds:
        current_round += 1
        actual_frequency = generate_random_frequency()

        # Play the tone for a short duration
        print(f"Round {current_round}: Listen to the tone.")
        # print(f"Round {current_round}/{max_rounds}: Listen to the tone at {actual_frequency:.2f} Hz ({frequency_to_pitch(actual_frequency)}).")

        play_tone(actual_frequency, sinewave, duration_ms=2000)

        # Get player's guess for the frequency
        guess_freq = get_user_input()

        # Calculate the score and update total score
        round_score = calculate_score(actual_frequency, guess_freq)
        score += round_score

        # Show feedback to the player
        feedback_text = f"Round {current_round}/{max_rounds}: Actual Frequency: {actual_frequency:.2f} Hz ({frequency_to_pitch(actual_frequency)}), Your Guess: {guess_freq} Hz, Score: {round_score}"
        print(feedback_text)

        # Wait for a short time before moving to the next round
        pygame.time.delay(1000)



    # Display the final score
    final_score_text = f"Game Over! Your Final Score: {score} / {1000*max_rounds}"
    print(final_score_text)

    sinewave.stop()
if __name__ == "__main__":
    main()
