import json
from flask import Flask, jsonify, request
from flask_cors import CORS

from Server.Utils.Voice import Voice

app = Flask(__name__)
CORS(app)


def load_config_file(config_path):
    # Load the configuration from the JSON file
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config


@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask server!'})


@app.route('/api/data', methods=['GET'])
def get_data():
    # Perform any necessary operations or retrieve data from a database
    data = {'data': [1, 2, 3, 4, 5]}
    return jsonify(data)


@app.route('/api/transcription_exchange', methods=['POST'])
def post_transcription():
    # Retrieve the string from the client request
    string_from_client = request.json.get('string')
    # Perform any necessary operations or retrieve data from a database
    data = {'transcription': string_from_client}
    return data


if __name__ == '__main__':
    config = load_config_file("configuration.json")
    voice_config = load_config_file("Utils/config_voice.json")
    voice_model = voice_config["emotions_models"]["Nervous"]

    # Example usage

    voice = Voice(config)
    text1 = ".Don't speak like that"
    voice.generate_emotional_speech(text1, voice_model)  # , filename="outputFix.wav")
    # voice.recognize_from_microphone_or_audio_file(audio_file_path="outputFix.wav")
    # app.run(debug=True)
