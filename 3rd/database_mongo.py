import pymongo

myclient = pymongo.MongoClient('mongodb://{}:{}@{}:{}/?authSource={}'.format("root","root","localhost","27017","efs"))

mydb = myclient.efs
k = mydb.collection_names(include_system_collections=True)  # 返回当前库下所有的collection名
print(k)


mycol = mydb["device"]
for x in mycol.find():
  print(x)