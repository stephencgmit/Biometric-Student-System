# Mongo introductory tutorial

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["userdb"]

mydb.create_collection(name)


#mydb = myclient["mydatabase2"]

#print(myclient.list_database_names())
