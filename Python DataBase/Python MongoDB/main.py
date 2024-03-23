import os
from bson.objectid import ObjectId

from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()

from pymongo.mongo_client import MongoClient # python -m pip install "pymongo[srv]"==3.11
mongo_acc = {
    'user': os.getenv("MONGODB_USER"),
    'password': os.getenv("MONGODB_PASSWORD")
}

uri = f"mongodb+srv://{mongo_acc['user']}:{mongo_acc['password']}@nodeapi.61bjodc.mongodb.net/?retryWrites=true&w=majority&appName=NodeAPI"

# Create a new client and connect to the server
client = MongoClient(uri)
dbname = client['myListUsers']
collections = dbname['users']


def create_db():
    try:
        process = True

        name = str(input("What's your name?\nr: "))
        print('')
        age = int(input("What's your age?\nr: "))
        print('')
        job = []

        while process:
            job.append(
                str(input("Type your job\nr: "))
            )
            print('')

            res = input("Finish (y/n)? ").upper()
            if res == "Y":
                process = False
            else:
                continue

        req = {'name': name, 'age': age, 'job': job}
        cursor = collections.insert_one(req)
        print(f"User created: {cursor.inserted_id}")
    
    except Exception as e:
        message = f"An Exception occured when inserting a document into `{collections}` Collection. "
        print(message, e)

def read_db():
    for item in collections.find():
        print(item)

def update_db():
    try:
        data_id = str(input("Set an Item ID\nr: "))

        new_values = { 
            "$set" : {
                'name' : "Python Update",
                'age' : 90,
                'job' : [
                    'Easy Language',
                    'Very Cool',
                    'Nice Program'
                ]
            }
        }

        query = { '_id' : ObjectId(data_id) }
        cursor = collections.update_one(query, new_values)

        print(f"User Updated: {cursor.matched_count} - {data_id}")
        print('')
        read_db()

    except Exception as e:
        message = f"An Exception occured when inserting a document into `{collections}` Collection. "
        print(message, e)

def delete_db():
    try:
        name = str(input("Set an User\nr: "))
        query = { 'name' : name }
        cursor = collections.delete_one(query)
        print('')
        
        print(f"User deleted: {cursor.deleted_count}")
        print('')
        read_db()

    except Exception as e:
        message = f"An Exception occured when inserting a document into `{collections}` Collection. "
        print(message, e)

def delete_db_by_id():
    try:
        data_id = str(input("Set an Item ID\nr: "))
        query = { '_id' : ObjectId(data_id) }
        cursor = collections.delete_one(query)
        print('')
        
        print(f"User deleted: {cursor.deleted_count} - {data_id}")
        print('')
        read_db()

    except Exception as e:
        message = f"An Exception occured when inserting a document into `{collections}` Collection. "
        print(message, e)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print('-=' * 35)
    print('')
    read_db()
    print('-' * 20)

    # create_db()
    
    # delete_db()
    # delete_db_by_id()

    update_db()

except Exception as e:
    print(e)