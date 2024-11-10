from typing import List


def create_query(fields: str) -> dict:
    """Generate a MongoDB query to fetch specific fields.

    Args:
        fields (list[str]): List of field names to include in the query.

    Returns:
        dict: MongoDB query for the specified fields.
    """
    return {field: 1 for field in fields}
