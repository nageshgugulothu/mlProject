from pymongo import MongoClient
import pandas as pd

# Replace <connection_string> with your MongoDB Atlas connection string
connection_string = ("mongodb+srv://nageshgugulothu:abcdef@cluster0.edjtkdn.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient(connection_string, ssl=True, ssl_cert_reqs='CERT_NONE')

# Replace <database_name> and <collection_name> with your actual database and collection names
db = client['nageshdb']
collection = db['thyroid']

# Retrieve all documents in the collection
documents = collection.find()

df = pd.DataFrame(list(documents))

print(df)



