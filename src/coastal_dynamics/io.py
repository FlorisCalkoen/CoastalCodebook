import json
from typing import Optional

import adlfs
import fsspec


def read_questions(
    blob_name: str, storage_options: Optional[dict[str, str]] = None
) -> dict:
    """
    Reads a JSON file from a local filesystem or Azure Blob storage.

    Args:
        blob_name (str): The blob name or local file path.
        storage_options (Optional[Dict[str, str]]): If given, contains options such as
            account name and SAS token for Azure Blob storage.

    Returns:
        Dict: The content of the JSON file.
    """
    # Use fsspec to handle both local and Azure Blob storage cases
    with fsspec.open(blob_name, "r", **(storage_options or {})) as f:
        questions = json.load(f)
    return questions


# BUG: will not write to cloud storage, but local stoarge. Keep here as template
# for later work. So this function (using fsspec) will replace write_questions
# below to make it morge storage agnostic.

# def write_questions(
#     processed_questions: dict,
#     blob_name: str,
#     storage_options: Optional[dict[str, str]] = None,
# ) -> None:
#     """
#     Writes a JSON file to a local filesystem or Azure Blob storage.

#     Args:
#         processed_questions (dict): The content to be written to the JSON file.
#         blob_name (str): The blob name or local file path.
#         storage_options (Optional[Dict[str, str]]): If given, contains options such as
#             account name and SAS token for Azure Blob storage.
#     """
#     # Use fsspec to handle both local and Azure Blob storage cases
#     with fsspec.open(blob_name, "w", **(storage_options or {})) as f:
#         json.dump(processed_questions, f, indent=4)


def write_questions(processed_questions, blob_name, storage_options):
    fs = adlfs.AzureBlobFileSystem(**storage_options)
    with fs.open(f"{blob_name}", mode="w") as f:
        json.dump(processed_questions, f, indent=4)
