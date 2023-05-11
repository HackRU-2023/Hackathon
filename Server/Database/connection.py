from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dbJeson import *

URI = "mongodb+srv://hackRuG36:th123456@cluster0.cooaizb.mongodb.net/?retryWrites=true&w=majority"

# mongodb://192.168.1.154:27017
class InitMongo:
    def __init__(self):
        self._client = MongoClient(URI, server_api=ServerApi('1'))
        try:
            self._client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
            raise e


    def __del__(self):
        self._client.close()

if __name__ == '__main__':
    db_connection = InitMongo()
    db_connection.set_agent(agent1)
    db_connection.set_agent(agent2)
    # db_connection.set_simulation(simulation1)
    # db_connection.set_simulation(simulation2)
    # db_connection.set_simulation(simulation3)
    # db_connection.set_simulation(simulation4)
    # db_connection.set_template_sim(template_simulation1)
    # db_connection.set_template_sim(template_simulation2)
    #db_connection.set_template_sim(agent_skills)

