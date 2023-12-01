from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from my_timer import timeit

global client, db, CONNECTED_TO_DB
CONNECTED_TO_DB = False


@timeit
def connect_to_db(username: str = 'aidanalrawi', password: str = 'aidan', db_name: str = 'marketing') -> None:
    global client, db, CONNECTED_TO_DB
    try:
        print(f"Connecting to DB: {db_name}...")
        uri = f"mongodb+srv://{username}:{password}@cluster0.reejb.mongodb.net/?retryWrites=true&w=majority"

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client[db_name]

        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        print(f"Pinged deployment. Successfully connected to DB: {db_name}.")

        CONNECTED_TO_DB = True

    except Exception as e:
        print(e)


def post_document(document: dict, collection_name: str):
    if not CONNECTED_TO_DB:
        connect_to_db()

    collection = db[collection_name]

    collection.insert_one(document)
    print(f"Successfully inserted {document} into {collection_name}.")


@timeit
def query_collection(query: dict, collection_name: str) -> list:
    if not CONNECTED_TO_DB:
        connect_to_db()
    collection = db[collection_name]

    queried_posts = [doc for doc in collection.find(query)]
    number_of_matches = collection.count_documents(query)
    print(f"Found {number_of_matches} posts matching the given query.")
    return queried_posts


@timeit
def delete_document(document: dict, collection_name: str):
    if not CONNECTED_TO_DB:
        connect_to_db()

    collection = db[collection_name]

    if query_collection(query=document, collection_name=collection_name):
        collection.delete_one(document)
        print(f"Successfully deleted {document['username']} from {collection_name}.")
    else:
        print(f"Could not find {document['username']} in {collection_name}.")


def get_collection_names():
    if not CONNECTED_TO_DB:
        connect_to_db()

    return db.list_collection_names()


def get_all_collection_keys(collection_name):
    if not CONNECTED_TO_DB:
        connect_to_db()

    collection = db[collection_name]
    keys = []
    for doc in collection.find():
        for field in doc.keys():
            if field not in keys and type(field) is str and field is not None:
                keys.append(field)

    return keys