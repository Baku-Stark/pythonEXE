import os
from bson.objectid import ObjectId

from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()

from pymongo.mongo_client import MongoClient # python -m pip install "pymongo[srv]"==3.11

class MongoDB_APP():
    mongo_acc = {
        'user': os.getenv("MONGODB_USER"),
        'password': os.getenv("MONGODB_PASSWORD")
    }

    uri = f"mongodb+srv://{mongo_acc['user']}:{mongo_acc['password']}@nodeapi.61bjodc.mongodb.net/?retryWrites=true&w=majority&appName=NodeAPI"

    # Create a new client and connect to the server
    client = MongoClient(uri)
    dbname = client['myListUsers']
    collections = dbname['users']

    def __init__(self):
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            print('-=' * 35)
            print('')
            self.read_db()
            print('-' * 20)

            # self.create_db()
            
            # self.delete_db()
            # self.delete_db_by_id()

            # self.update_db()

        except Exception as e:
            print(e)


    def create_db(self, req: object):
        """
            Mongo DB create function
        """
        try:
            cursor = self.collections.insert_one(req)
            print(f"User created: {cursor.inserted_id}")
        
        except Exception as e:
            message = f"An Exception occured when inserting a document into `{self.collections}` Collection. "
            print(message, e)

    def read_db(self):
        for item in self.collections.find():
            print(item)

    def update_db(self, data_id: str, req: object):
        try:
            new_values = { "$set" : req }

            query = { '_id' : ObjectId(data_id) }
            cursor = self.collections.update_one(query, new_values)

            print(f"User Updated: {cursor.matched_count} - ID: {data_id}")
            print('')
            self.read_db()

        except Exception as e:
            message = f"An Exception occured when inserting a document into `{self.collections}` Collection. "
            print(message, e)

    def delete_db(self, name: str):
        try:
            query = { 'name' : name }
            cursor = self.collections.delete_one(query)
            print('')
            
            print(f"User deleted: {cursor.deleted_count}")
            print('')
            self.read_db()

        except Exception as e:
            message = f"An Exception occured when inserting a document into `{self.collections}` Collection. "
            print(message, e)

    def delete_db_by_id(self, data_id: str):
        try:
            query = { '_id' : ObjectId(data_id) }
            cursor = self.collections.delete_one(query)
            print('')
            
            print(f"User deleted: {cursor.deleted_count} - {data_id}")
            print('')
            self.read_db()

        except Exception as e:
            message = f"An Exception occured when inserting a document into `{self.collections}` Collection. "
            print(message, e)