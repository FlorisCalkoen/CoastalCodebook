import os

import toml

# Get the directory containing the current file.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Parse the pyproject.toml
pyproject_config = toml.load(os.path.join(BASE_DIR, "..", "..", "pyproject.toml"))

__version__ = pyproject_config["tool"]["poetry"]["version"]
