# Flask Text-to-Speech

This is a Flask web application that converts a JSON file containing transcribed text to an audio file using the gTTS (Google Text-to-Speech) library. 

## Installation

1. Clone the repository.
2. Install the required dependencies using `pip install flask gTTS pydub`.
3. Run the application using `python app.py`.

## Usage

1. Open the web application in your browser by visiting http://localhost:5000.
2. Upload a JSON file containing transcribed text using the "Choose File" button.
3. Click the "Upload" button to submit the file.
4. Wait for the audio file to be generated.
5. Click the "Download" button to download the audio file.

## Notes

- The JSON file must be in the following format:


```json
[
  {
    "start": 0,
    "duration": 4.59,
    "transcript": "This is the first sentence."
  },
  {
    "start": 4.59,
    "duration": 6.21,
    "transcript": "This is the second sentence."
  }
]
```

- The audio file will be generated in the `output` folder.
- The web application will only generate audio files in MP3 format.
- The web application is intended for personal and educational use only.
- The gTTS library uses the Google Text-to-Speech API, which may have usage limits and/or require authentication.
