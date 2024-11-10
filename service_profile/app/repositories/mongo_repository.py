from pymongo import MongoClient
from app.config.settings import DATABASE_URL

client = MongoClient(DATABASE_URL)
db = client["service_profile"]

async def save_to_mongo(key: str, data: dict):
    """Save data to MongoDB with a unique key.

    Args:
        key (str): Unique identifier for the document.
        data (dict): Data to be saved.
    """
    db.profiles.insert_one({"_id": key, **data})

async def fetch_from_mongo(query: dict):
    """Fetch data from MongoDB based on a query.

    Args:
        query (dict): MongoDB query filter.

    Returns:
        dict: The document matching the query.
    """
    return db.profiles.find_one(query)
