import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

environment = os.getenv("ENVIRONMENT", "staging")

if environment == "staging":
    from config.staging import DATABASE
elif environment == "preprod":
    from config.preprod import DATABASE
elif environment == "prod":
    from config.prod import DATABASE
else:
    raise ValueError("Invalid environment")

client = MongoClient(os.getenv("MONGO_URI"))
students = client[DATABASE]["students"]


# CREATE
def create_student(name):
    students.insert_one({"name": name})


# READ
def get_students():
    return list(students.find({}, {"_id": 0}))


# UPDATE
def update_student(name, new_name):
    students.update_one({"name": name}, {"$set": {"name": new_name}})


# DELETE
def delete_student(name):
    students.delete_one({"name": name})


print(get_students())
create_student("Al")
