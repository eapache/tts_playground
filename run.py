print("Loading...")

from TTS.api import TTS
import sounddevice as sd
import sys

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")

def play(string):
  string = "\n".join([line for line in string.splitlines() if line.strip()])
  if not string:
    return
  if len(sys.argv) > 1:
    audio = tts.tts_with_vc(text=string, speaker_wav=sys.argv[1], language="en")
  else:
    audio = tts.tts(text=string, speaker="Daisy Studious", language="en")
  sd.play(audio, samplerate=22050)
  sd.wait()

play("Hello world!")

try:
  while True:
    play(input("> "))
except KeyboardInterrupt:
  print("\nExiting...")
