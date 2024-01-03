import fluidsynth

def play_soundfont_note(soundfont_file, note_number, duration_ms):
    # Initialize FluidSynth and set the SoundFont file
    fs = fluidsynth.Synth()
    fs.start(driver="alsa")  # Use "alsa" for Linux or "coreaudio" for macOS

    sfid = fs.sfload(soundfont_file)
    fs.program_select(0, sfid, 0, 0)  # Select the instrument

    # Note-on event
    fs.noteon(0, note_number, 80)

    # Sleep to let the note play
    import time
    time.sleep(duration_ms / 1000.0)

    # Note-off event
    fs.noteoff(0, note_number)

    # Clean up
    fs.delete()

if __name__ == "__main__":
    # Path to the SoundFont file
    # soundfont_file = "path_to_your_soundfont_file.sf2"
    soundfont_file = "C:/Users/jjrba/Code_Projects/Libraries/GeneralUser GS 1.471/GeneralUser GS v1.471.sf2"

    # Note number (e.g., 60 for C4)
    note_number = 60

    # Duration in milliseconds
    duration_ms = 1000

    # Play the note
    play_soundfont_note(soundfont_file, note_number, duration_ms)
