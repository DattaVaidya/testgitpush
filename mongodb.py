import pymongo
client = pymongo.MongoClient("mongodb+srv://dattavaidya1:Datta117711@cluster0.rwdzoar.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d11={
    "name":"datta",
    "surname":"vaidya",
    "email_id":"dattavaidya1@gmail.com"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)