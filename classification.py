import pandas as pd
import numpy as np
from pymongo import MongoClient
from IPython.display import display

# Connect to MongoDBAtlas
client = MongoClient("mongodb://alexandros9901:1234@ac-4szu7xo-shard-00-00.fmifbmq.mongodb.net:27017,ac-4szu7xo-shard-00-01.fmifbmq.mongodb.net:27017,ac-4szu7xo-shard-00-02.fmifbmq.mongodb.net:27017/?ssl=true&replicaSet=atlas-b5opm8-shard-0&authSource=admin&appName=TestCluster")

# Select the database

db = client["analytics"]

collection = db["clickstream"]

# Retrieve documents

data = list(collection.find())

df = pd.DataFrame(data)


display(df)


# Overview of descriptive analytics

print(df.describe())

# Check datatypes

print(df.info())