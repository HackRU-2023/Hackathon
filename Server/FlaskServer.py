import json

from bson import json_util
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

# @app.route('/api/users/<id>', methods=['GET'])
# def login(id):

@app.route('/api/login', methods=['GET'])
def login():
    agent = {

        "id": id
    }
    # Perform any necessary operations or retrieve data from a database
<<<<<<< HEAD
    agent_details = db.get_agent(agent)
    return jsonify(agent_details)
=======
    agent_login = db.get_agent(agent)
    return jsonify(agent_login)

>>>>>>> 40c25b4137b302532827dfa4a18dfe1e8a8a1695

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
    skills = db.set_template_sim()
    # Convert ObjectId to string
    skills = json.loads(json_util.dumps(skills))

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


# company_description, emotions, personality, call_subject
@app.route('/api/situation_description', methods=['POST'])
def get_company_description():
    emotions = request.json.get('emotions')
    personality = request.json.get('personality')
    situation_description = request.json.get('situation_description')
    simulation_id = simulator.start_simulation(config["A company that provide internet"], emotions,
                                               personality,
                                               situation_description)


if __name__ == '__main__':

    db_connection = InitMongo()
    db = DataBase(db_connection)
    config = load_config_file("configuration.json")
    local_config = load_config_file("local_conf.json")
    voice_config = load_config_file("Utils/config_voice.json")
    emotions_models = voice_config["emotions_models"]

    simulator = OpenAISimulator()
    simulation_id = None

    voice = Voice(local_config)

    app.run(debug=True)
