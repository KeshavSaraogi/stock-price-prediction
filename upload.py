import boto3
import os
from process_data import process_stock_data


def upload_to_s3(file_name, bucket_name):
    s3 = boto3.client("s3")
    try:
        s3.upload_file(file_name, bucket_name, os.path.basename(file_name))
        print(f"{file_name} uploaded to S3 bucket {bucket_name}")
    except Exception as e:
        print(f"Error uploading to S3: {e}")

if __name__ == "__main__":
    ALPHA_VANTAGE_API_KEY = "your-alpha-vantage-api-key"
    SYMBOL = "IBM"
    S3_BUCKET_NAME = "stock-data-api"

    files_to_upload = process_stock_data(SYMBOL, ALPHA_VANTAGE_API_KEY)

    if files_to_upload:
        for file in files_to_upload:
            if os.path.exists(file):
                upload_to_s3(file, S3_BUCKET_NAME)
            else:
                print(f"File {file} not found.")
