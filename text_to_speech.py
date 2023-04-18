import json
import os
from gtts import gTTS
from pydub import AudioSegment

# Create the output folder if it does not exist
if not os.path.exists("output"):
    os.makedirs("output")

# Load the JSON data from a local file
with open("transcript.json", "r") as file:
    data = json.load(file)

# Process each segment
audio_segments = []

for i, segment in enumerate(data):
    # Convert the transcript text to audio
    transcript = segment["transcript"]
    tts = gTTS(text=transcript, lang='en')
    audio_file = f"audio_{i}.mp3"
    tts.save(audio_file)

    # Load the generated audio using pydub
    audio_segment = AudioSegment.from_mp3(audio_file)
    audio_segments.append(audio_segment)

    # Remove the temporary audio file
    os.remove(audio_file)

# Concatenate the audio segments
final_audio = sum(audio_segments)

# Export the final audio to the output folder
final_audio.export("output/output_audio.mp3", format="mp3")
