import json
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from bson import json_util





from Server.Database.connection import InitMongo
from Server.Database.dataBase import DataBase
from Server.Simulator.OpenAISimulator import OpenAISimulator
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

@app.route('/api/users/<id>', methods=['GET'])
def login(id):
    agent = {

        "id": id
    }
    # Perform any necessary operations or retrieve data from a database
    agent_details = db.get_agent(agent)
    return jsonify(agent_details)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Perform any necessary operations or retrieve data from a database
    data = {'data': [1, 2, 3, 4, 5]}
    return jsonify(data)

@app.route('/api/skills_fill', methods=['GET'])
def get_skills_to_fill():
    # Perform any necessary operations or retrieve data from a database
    skills = db.get_client_skills()
    # Convert ObjectId to string
    skills = json.loads(json_util.dumps(skills))

    return jsonify(skills)


@app.route('/api/skills_template', methods=['GET'])
def get_skills_template():
    # Perform any necessary operations or retrieve data from a database
    skills = db.get_client_skills()
    return jsonify(skills)

@app.route('/api/skills_agent_template', methods=['GET'])
def get_skills_agent_template():
    # Perform any necessary operations or retrieve data from a database
    skills = db.get_client_skills()
    return jsonify(skills)

@app.route('/api/transcription_exchange', methods=['POST'])
def post_transcription():
    # Retrieve the string from the client request
    string_from_client = request.json.get('transcript')
    # Perform any necessary operations or retrieve data from a database

    #################################
    if string_from_client == "review":
        result = simulator.review_simulation(simulation_id)
        return result
    else:
        result, emotion = simulator.generate_answer(simulation_id, string_from_client)
        if emotion not in emotions_models:
            emotion = "NATURAL"

        voice.generate_emotional_speech(result, emotions_models[emotion], "audio/curr_speech_file.wav")
    print(result)
    return send_file("audio/curr_speech_file.wav", mimetype='audio/x-wav')
    ############################


if __name__ == '__main__':
    print("try")
    config = load_config_file("configuration.json")
    voice_config = load_config_file("Utils/config_voice.json")
    emotions_models = voice_config["emotions_models"]

    ########################################################
    simulator = OpenAISimulator()
    simulation_id = simulator.start_simulation('A company that provide internet', "Angry, disappointed",
                                               "Young man usually friendly",
                                               "He paying for 100mb internet but only get 5mb after internet check")

    #########################################################
    # Example usage

    voice = Voice(config)
    db_connection = InitMongo()
    db = DataBase(db_connection)
    # text1 = ".Don't speak like that"
    # voice.generate_emotional_speech(text1, voice_model)  # , filename="outputFix.wav")
    # voice.recognize_from_microphone_or_audio_file(audio_file_path="outputFix.wav")
    app.run(debug=True)
