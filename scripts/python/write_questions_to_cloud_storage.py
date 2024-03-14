import argparse
import logging
import os
import sys
from pathlib import Path

import dotenv
import fsspec


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Upload a JSON file to a cloud container."
    )
    parser.add_argument("file_path", type=Path, help="Path to the JSON file to upload.")
    parser.add_argument(
        "cloud_href",
        type=str,
        help="Href to the cloud container, e.g., 'az://bucket_name/path/*.json'",
    )
    return parser.parse_args()


def load_environment():
    """Load environment variables."""
    dotenv.load_dotenv(override=True)
    sas_token = os.getenv("AZURE_STORAGE_SAS_TOKEN")
    account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
    if not all([sas_token, account_name]):
        logging.error("Environment variables for Azure storage are not properly set.")
        sys.exit(1)
    return {"account_name": account_name, "sas_token": sas_token}


def upload_file(file_path, cloud_href, storage_options):
    """Upload a JSON file to the specified cloud storage container."""
    with fsspec.open(file_path, "rb") as src_file:
        json_data = src_file.read()

    with fsspec.open(cloud_href, "wb", **storage_options) as f:
        f.write(json_data)


def main():
    """Main function to orchestrate the upload of a JSON file."""
    args = parse_arguments()
    storage_options = load_environment()

    try:
        upload_file(args.file_path, args.cloud_href, storage_options)
        logging.info(
            f"File {args.file_path} uploaded successfully to {args.cloud_href}."
        )
    except Exception as e:
        logging.error(f"Failed to upload file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
