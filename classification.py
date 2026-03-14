import pandas as pd
import numpy as np
from pymongo import MongoClient
from IPython.display import display
from dotenv import load_dotenv

# Connect to MongoDBAtlas
client = MongoClient("MONGODB_CLUSTER")

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