from flask import Flask, render_template, request, send_from_directory
import os
import json
from gtts import gTTS
from pydub import AudioSegment

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'output'

if not os.path.exists(app.config['OUTPUT_FOLDER']):
    os.makedirs(app.config['OUTPUT_FOLDER'])

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


def process_json(data, voice, speed):
    audio_segments = []

    for i, segment in enumerate(data):
        transcript = segment["transcript"]
        tts = gTTS(text=transcript, lang='en', tld=voice)
        audio_file = f"audio_{i}.mp3"
        tts.save(audio_file)

        audio_segment = AudioSegment.from_mp3(audio_file)
        altered_audio_segment = audio_segment._spawn(
            audio_segment.raw_data, overrides={
                "frame_rate": int(audio_segment.frame_rate * float(speed))}
        )
        audio_segments.append(altered_audio_segment)
        os.remove(audio_file)

    final_audio = sum(audio_segments)
    final_audio.export(
        f"{app.config['OUTPUT_FOLDER']}/output_audio.mp3", format="mp3")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    json_file = request.files['json_file']
    voice = request.form['voice']
    speed = request.form['speed']
    json_path = os.path.join(app.config['UPLOAD_FOLDER'], 'transcript.json')
    json_file.save(json_path)

    with open(json_path, 'r') as file:
        data = json.load(file)

    process_json(data, voice, speed)
    return {'result': 'success'}


@app.route('/download')
def download():
    return send_from_directory(app.config['OUTPUT_FOLDER'], 'output_audio.mp3')


if __name__ == '__main__':
    app.run(debug=True)
