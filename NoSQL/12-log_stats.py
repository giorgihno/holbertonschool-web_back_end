#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB
    Database: logs
    Collection: nginx
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the database and collection
    db = client.logs
    collection = db.nginx
    
    # Get total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Display Methods
    print("Methods:")
    
    # Count documents for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Count documents with method=GET and path=/status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
