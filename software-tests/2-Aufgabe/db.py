from pymongo import MongoClient

from user import *


class DB:
    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self.collection = self.client["aufgabe-2"]["user"]

    def set_user(self, user: User):
        self.collection.insert_one(user.__dict__)

    def get_user(self) -> User:
        db_user = self.collection.find_one()
        return User(db_user["name"], db_user["email"])

    def close(self):
        self.client.close()
