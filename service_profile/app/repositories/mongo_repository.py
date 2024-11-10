from pymongo import MongoClient
from app.config.settings import DATABASE_URL

client = MongoClient(DATABASE_URL)

async def save_to_mongo(key: str, data: dict, client_param: str):
    """Save data to MongoDB with a unique key.

    Args:
        key (str): Unique identifier for the document.
        data (dict): Data to be saved.
    """
    db = client[client_param]
    db.profiles.insert_one({"_id": key, **data})

async def fetch_from_mongo(query: dict, client_param: str):
    """Fetch data from MongoDB based on a query.

    Args:
        query (dict): MongoDB query filter.

    Returns:
        dict: The document matching the query.
    """
    db = client[client_param]
    return db.profiles.find_one(query)
