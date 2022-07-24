import pymongo
client = pymongo.MongoClient("mongodb+srv://saicharan:mongodb123@sai.s2wz1zt.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['MyInfo']
collection = database['sai']

# record = collection.find()
# for i in record:
#     print(i)

#data = collection.find({"companyName":"iNeuron"})
data = collection.find({"courseOffered":{"$gt":"E"}}) # course offered greater than E
for i in data:
    print(i)