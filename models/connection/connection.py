from pymongo import MongoClient
from models.connection.mongodb_credentials import *

class DBConnectionHandler:
    def __init__(self):
        #mongodb://localhost:27017
        self.connection_string = 'mongodb://{}:{}'.format(
            #MONGO_USER,
            #MONGO_PASSWORD,
            MONGO_HOST,
            MONGO_PORT
        )
        print(self.connection_string)

        self.db_name = MONGO_DB_NAME
        self.client = None
        self.connection = None

    def connect_to_db(self):
        self.client = MongoClient(self.connection_string)
        self.connection = self.client[self.db_name]

    def get_db_connection(self):
        return self.connection

