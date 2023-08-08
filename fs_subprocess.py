import mido
import subprocess

# Paths to FluidSynth executable and SoundFont
fluidsynth_executable = "C:/tools/fluidsynth/bin/fluidsynth.exe"
soundfont_path = "C:/tools/soundfonts/GeneralUser GS 1.471/GeneralUser GS v1.471.sf2"

# Create a MIDI message for the desired note (60 corresponds to middle C)
note_number = 60
note_on = mido.Message("note_on", note=note_number, velocity=64, time=0)
note_off = mido.Message("note_off", note=note_number, velocity=0, time=100)

# Write the MIDI messages to a temporary MIDI file
temp_midi_file = "temp.mid"
with mido.MidiFile() as midi_file:
    midi_file.tracks.append([note_on, note_off])
    midi_file.save(temp_midi_file)

# Command to play the temporary MIDI file using FluidSynth
command = [
    fluidsynth_executable,
    "-o",
    "audio.driver=dsound",  # Use the DirectSound audio driver
    soundfont_path,
    temp_midi_file
]

# Run the FluidSynth command
subprocess.run(command, shell=True)

# Clean up the temporary MIDI file
import os
os.remove(temp_midi_file)
