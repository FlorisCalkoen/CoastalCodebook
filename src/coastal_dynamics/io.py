import json
from typing import Any

import fsspec


def load_questions(
    href_or_fp: str, storage_options: dict[str, Any] | None = None
) -> dict[str, Any]:
    """
    Loads a JSON file from a given file path or URL using fsspec and returns its content as a dictionary.

    Args:
        href_or_fp (str): The file path or URL of the JSON file to be loaded.
        storage_options (Optional[Dict[str, Any]]): Additional options for configuring access to the file system,
            such as credentials. Defaults to None, which means no additional options are used.

    Returns:
        Dict[str, Any]: A dictionary representing the JSON file's content.

    Raises:
        JSONDecodeError: If the JSON file is not properly formatted.
        FileNotFoundError: If the file does not exist at the specified path or URL.
    """
    with fsspec.open(href_or_fp, "r", **(storage_options or {})) as f:
        questions = json.load(f)

    return questions
