from pymongo import MongoClient


conn = MongoClient('mongodb+srv://bruno:canela@gama.9tcj4nl.mongodb.net/test')

print(conn.list_database_names())