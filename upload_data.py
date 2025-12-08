from pymongo.mongo_client import MongoClient
import pandas as pd
import json
url="mongodb+srv://kranthi:NwtPxSWouijDe4hp@cluster0.dqik7.mongodb.net/?appName=Cluster0"
client = MongoClient(url)
DATABASE_NAME="Venkat"
COLLECTION_NAME="waferfault"
df=pd.read_csv("C:\Users\kranthi-418\OneDrive\Desktop\placement project 1\artifacts\placement data.xlsx")
df=df.drop("Unnamed: 0",axis=1)
json_record=list(json.loads(df.T.to_json()).values())
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)