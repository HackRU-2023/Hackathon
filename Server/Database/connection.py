from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


URI = "<secret_uri>"


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

