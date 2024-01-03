Set objShell = CreateObject("WScript.Shell")
soundfontPath = "C:\tools\soundfonts\GeneralUser GS 1.471\GeneralUser GS v1.471.sf2"
midiFilePath = "C:\tools\soundfonts\GeneralUser GS 1.471\demo MIDIs\earthday.mid"

command = """C:\tools\fluidsynth\bin\fluidsynth.exe"" -o audio.driver=dsound -g 1.0 -ni """ & soundfontPath & """ """ & midiFilePath & """"

objShell.Run command, 0, True
