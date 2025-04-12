import os
from infra.mongodb_connector import MongoDBConnector
import pandas as pd

def query_and_export():
    # Load environment variables
    mongo_uri = os.getenv("MONGO_URI", "mongodb://admin:password@mongodb:27017/")
    mongo_db = os.getenv("MONGO_DB", "scrapy_db")

    # Connect to MongoDB
    connector = MongoDBConnector(mongo_uri, mongo_db)
    
    try:
        # Fetch all data from json_data collection using reusable query
        data = connector.get_items("json_data")
        
        if not data:
            print("No data found in json_data collection.")
            return

        # Convert to DataFrame, flattening nested fields
        df = pd.json_normalize(data)
        
        # Export to CSV
        output_file = "jobs_project/final_jobs.csv"
        df.to_csv(output_file, index=False, encoding="utf-8")
        print(f"Data exported to {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connector.close()

if __name__ == "__main__":
    query_and_export()