import json

from bson import json_util
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
# from Utils import InitUtil as IU
from bson import json_util

from Server.Database.connection import InitMongo
from Server.Database.dataBase import DataBase
from Server.Models.agent import Agent
from Server.Simulator.OpenAISimulator import OpenAISimulator
from Server.Utils.Voice import Voice

app = Flask(__name__)
CORS(app)
emotion = "NATURAL"


def get_client_agent_strongs(db):
    agent = db.get_agent("NglT4UH7dzTYD6EEmW64NvzKQZ82")
    agent_skills = agent.skills
    client_skills = db.get_client_skills_yuval()

    client_personals = client_skills[0]
    client_emotions = client_skills[1]
    return agent_skills, client_personals, client_emotions


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


@app.route('/api/get_agent', methods=['GET'])
def get_agent():
    agent_id = request.json.get('agent_id')
    agent = db.get_login(agent_id)
    agent = json.loads(json_util.dumps(agent))
    return jsonify(agent)


@app.route('/api/skills_template', methods=['GET'])
def get_skills_template():
    # Perform any necessary operations or retrieve data from a database
    skills = db.get_template_sim()
    # Convert ObjectId to string
    skills = json.loads(json_util.dumps(skills))
    return jsonify(skills)


@app.route('/api/get_review', methods=['GET'])
def get_review():
    result = simulator.review_simulation(simulation_id)
    return jsonify(result)


# @app.route('/api/simulation_finish', methods=['POST'])
# def post_finish_simulation():
#     update_sim_finish

@app.route('/api/transcription_exchange', methods=['POST'])
def post_transcription():
    # Retrieve the string from the client request
    string_from_client = request.json.get('transcript')
    # Perform any necessary operations or retrieve data from a database

    #################################
    # if string_from_client == "review":
    #     result = simulator.review_simulation(simulation_id)
    #     return result
    # else:
    result, emotion = simulator.generate_answer(simulation_id, string_from_client)
    if emotion not in emotions_models:
        emotion = "NATURAL"

    voice.generate_emotional_speech(result, emotions_models[emotion], "audio/curr_speech_file.wav")
    print(result)
    return send_file("audio/curr_speech_file.wav", mimetype='audio/x-wav')
    ############################


# company_description, emotions, personality, call_subject
@app.route('/api/emotion', methods=['GET'])
def get_client_emotion():
    return emotion


# company_description, emotions, personality, call_subject
@app.route('/api/situation_description', methods=['POST'])
def get_company_description():
    emotions = request.json.get('emotions')
    personality = request.json.get('personality')
    situation_description = request.json.get('situation_description')
    simulation_id = simulator.start_simulation(config["A company that provide internet"], emotions,
                                               personality,
                                               situation_description)


@app.route('/api/convertEmotions', methods=['GET'])
def convert_emotions():
    agent_id = request.json.get('agent_id')
    agent = db.get_agent(agent_id)  # type: Agent
    skills = agent.skills
    # client_emotions = ["CALM", "ANGRY", "HAPPY", "SURPRISED", "HOPEFUL",
    #                    "CONFUSED", "DISAPPOINTED", "NATURAL"]
    # client_qualifies = ["empathy", "patience", "fast talk", "stuttering speech",
    #                     "weak voice", "monotonous speech", "rude", "stingy",
    #                     "gentle", "assertive", "manipulative"]
    c_emotion_scores = {"CALM": 7, "ANGRY": 5, "HAPPY": 2, "SURPRISED": 0, "HOPEFUL": 4,
                        "CONFUSED": 3, "DISAPPOINTED": 9, "NATURAL": 7}
    c_qualifies_scores = [int(skills["empathy"]),
                          int(skills["patience"]),
                          int(skills["expressiveness"]),
                          int(skills["emotional management"]),
                          int(skills["expressiveness"]),
                          int(skills["listening"]),
                          int(skills["empathy"]),
                          int(skills["emotional management"]) * 0.20 + 0.8 * int(skills["expressiveness"]),
                          int(skills["expressiveness"]),
                          int(skills["emotional management"]),
                          int(skills["empathy"])]
    chosen_emotion = [key for key, value in c_emotion_scores.items() if value == max(c_emotion_scores.values())]
    chosen_emotion = chosen_emotion[0]
    result = {
        "chosen_emotion": chosen_emotion[0],
        "qualifies_scores": c_qualifies_scores
    }
    return jsonify(result)


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
    # res = IU.InitUtil.matching_customer(simulator.model_engine,db)
    app.run(debug=True)
