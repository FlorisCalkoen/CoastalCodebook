import argparse
import logging
import os
import pathlib
import sys

import dotenv

import coastal_dynamics as cd


def process_questions(questions):
    """Process and hash answers within the questions dictionary based on question type."""
    for _, q_data in questions.items():
        q_data["answer"] = cd.hash_answer(q_data.get("answer"), q_data.get("type"))
    return questions


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Process questions from cloud storage."
    )
    parser.add_argument(
        "fname", type=str, help="The file for the questions file to process"
    )
    return parser.parse_args()


def load_environment():
    """Load environment variables."""
    dotenv.load_dotenv(override=True)
    sas_token = os.getenv("AZURE_STORAGE_SAS_TOKEN")
    storage_account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
    if not all([sas_token, storage_account_name]):
        logging.error("Environment variables for Azure storage are not properly set.")
        sys.exit(1)
    return {"account_name": storage_account_name, "sas_token": sas_token}


def process_file(storage_options, blob_name):
    """Process a single file."""
    fstem = pathlib.Path(blob_name).stem
    hashed_blob_name = f"coastal-dynamics/questions/{fstem}_hashed.json"

    questions = cd.read_questions(blob_name, storage_options)
    processed_questions = process_questions(questions)
    cd.write_questions(processed_questions, hashed_blob_name, storage_options)


def main():
    """Main function to orchestrate the processing of questions."""
    args = parse_arguments()
    storage_options = load_environment()
    blob_name = f"az://coastal-dynamics/questions/{pathlib.Path(args.fname).stem}.json"

    try:
        process_file(storage_options, blob_name)
        logging.info("Questions processed and stored successfully.")
    except Exception as e:
        logging.error(f"Failed to process questions: {e}")
        sys.exit(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
