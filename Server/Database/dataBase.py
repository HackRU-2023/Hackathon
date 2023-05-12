import json

from Server.Database.connection import InitMongo
from Server.Database.dbJeson import *
from Server.Models.agent import Agent
from Server.Models.simulation import Simulation



class DataBase:
    def __init__(self,db_connection):
        db_connection = db_connection
        self.mydb = db_connection._client["HackRu"]

    def get_login(self, id):
        user_name = ""
        password = ""
        position = ""
        skills = ""
        simulation = ""
        mycol = self.mydb["agents"]
        myquery = {"id": id}
        mydoc = mycol.find(myquery)
        # for key in mydoc:
        #     user_name = key['user_name']
        #     password = key['password']
        #     position = key['position']
        #     skills = key['skills']
        #     simulation = key['simulation']
        # agent = Agent(user_name, password, id, position, skills, simulation)
        # jsonStr = json.dumps(agent.__dict__)
        return mydoc

    def get_agent(self, id):
        user_name = ""
        password = ""
        position = ""
        skills = ""
        simulation = ""
        mycol = self.mydb["agents"]
        myquery = {"id": id}
        mydoc = mycol.find(myquery)
        for key in mydoc:
            user_name= key['user_name']
            password = key['password']
            position = key['position']
            skills = key['skills']
            simulation = key['simulation']
        agent = Agent(user_name, password,id,position,skills,simulation)
        jsonStr = json.dumps(agent.__dict__)
        return agent

    def get_client_skills(self):
        mycol = self.mydb["clientSkills"]
        mydoc = mycol.find()
        return mydoc

    def get_client_skills_yuval(self):
        mycol = self.mydb["clientSkills"]
        mydoc = mycol.find()
        client_skills = []
        for x in mydoc:
            personal = x['personal']
            em = x['emotion']
        client_skills.append(personal)
        client_skills.append(em)
        return client_skills

    def get_template_sim(self):
        mycol = self.mydb["templateSimulation"]
        mydoc = mycol.find()
        return mydoc

    def set_simulation(self, sim):
        mycol = self.mydb["simulations"]
        result = mycol.insert_one(sim)
        if result.inserted_id:
            print("Insert Simulation Successfully")

    def update_simulation(self,sim):
        mycol = self.mydb["simulations"]
        myquery = {"id": sim.id}
        newvalues = {"$set": {"training_skills":  sim.summary, "recording": sim.recording, "status": sim.status}}
        mycol.update_one(myquery, newvalues)

    def update_agent(self,agent):
        mycol = self.mydb["agents"]
        myquery = {"id": agent.id}
        myupdate = {"$push": {"simulation": agent.simulation[-1]},
                    "$set": {"skills.listening":  agent.skills['listening'],
                             "skills.patience":  agent.skills['patience'],
                             "skills.empathy":  agent.skills['empathy'],
                             "skills.professional":  agent.skills['professional'],
                             "skills.emotional management":  agent.skills['emotional management'],
                             "skills.coping with stressful situations":  agent.skills['coping with stressful situations'],
                             "skills.expressiveness":  agent.skills['expressiveness']}}
        mycol.update_one(myquery, myupdate)

    def set_agent(self, agent):
        mycol = self.mydb["agents"]
        result = mycol.insert_one(agent)
        print(result.inserted_id)

    def set_template_sim(self, sim):
        mycol = self.mydb["templateSimulation"]
        result = mycol.insert_one(sim)
        if result.inserted_id:
            print("Insert Simulation Successfully")


db_connection = InitMongo()
db = DataBase(db_connection)
