import pymongo
client=pymongo.MongoClient("mongodb+srv://sarthakr90:DEHturbine2022@sarthak.hv5ng.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={
    "name":"Sarthak",
    "email" : "sarthakrout.90@gmail.com",
    "surname" : "rout"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)