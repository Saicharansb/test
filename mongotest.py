import pymongo
client = pymongo.MongoClient("mongodb+srv://saicharan:mongodb123@sai.s2wz1zt.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d ={
    "name":"Saicharan",
    "email":"sbhavanipetwar@gmail.com",
    "surname":"Sam"


}
db1= client['mongotest']
coll =db1['test']
coll.insert_one(d)