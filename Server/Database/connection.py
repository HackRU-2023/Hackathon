from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
#from dbJeson import *

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

