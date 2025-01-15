import os
import boto3
from botocore.exceptions import NoCredentialsError

s3 = boto3.client(
    's3',
    endpoint_url=os.getenv('AWS_ENDPOINT_URL', 'http://hload-localstack:4566'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', 'test'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', 'test'),
    region_name='us-east-1'
)

BUCKET_NAME = os.getenv('AWS_BUCKET_NAME', 'hload-bucket')


def create_bucket_if_not_exists(bucket_name: str):
    # Перевіряємо, чи існує бакет
    existing_buckets = s3.list_buckets()
    if not any(bucket['Name'] == bucket_name for bucket in existing_buckets['Buckets']):
        # Створюємо бакет, якщо його немає
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} created.")


def upload_to_s3(file_content: bytes, file_name: str) -> str:
    try:
        create_bucket_if_not_exists(BUCKET_NAME)  # Перевірка і створення бакета
        s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_content)
        return f"s3://{BUCKET_NAME}/{file_name}"
    except NoCredentialsError:
        raise Exception("Credentials not available")
