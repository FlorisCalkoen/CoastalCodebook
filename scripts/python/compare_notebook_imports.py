# import argparse
# import logging
# import re
# from pathlib import Path

# import nbformat
# import yaml

# logging.basicConfig(level=logging.INFO)


# def extract_imports_from_notebook(notebook_path: Path) -> set[str]:
#     """
#     Extracts all imports from a Jupyter notebook.

#     Args:
#         notebook_path (Path): Path to the Jupyter notebook.

#     Returns:
#         Set[str]: A set containing all unique imports from the notebook.
#     """
#     with notebook_path.open() as f:
#         notebook = nbformat.read(f, as_version=4)

#     imports = set()
#     for cell in notebook.cells:
#         if cell.cell_type == "code":
#             imports.update(_extract_imports_from_code(cell.source))

#     return imports


# def extract_imports_from_python(python_path: Path) -> set[str]:
#     """
#     Extracts all imports from a Python file.

#     Args:
#         python_path (Path): Path to the Python file.

#     Returns:
#         Set[str]: A set containing all unique imports from the Python file.
#     """
#     with python_path.open() as f:
#         code = f.read()

#     return _extract_imports_from_code(code)


# def _extract_imports_from_code(code: str) -> set[str]:
#     """
#     Extracts import statements from a code string.

#     Args:
#         code (str): The code string to extract imports from.

#     Returns:
#         Set[str]: A set of unique imports extracted from the code.
#     """
#     matches = re.findall(
#         r"^\s*(?:from\s+([\w\.]+)\s+)?import\s+([\w\.]+)",
#         code,
#         re.MULTILINE,
#     )
#     imports = set()
#     for match in matches:
#         if match[0]:
#             imports.add(match[0].split(".")[0])  # Take only the top-level module
#         imports.add(match[1].split(".")[0])  # Same for direct imports

#     return imports


# def extract_libraries_from_environment_yml(yml_path: Path) -> dict[str, str]:
#     """
#     Extracts dependencies from an environment.yml file.

#     Args:
#         yml_path (Path): Path to the environment.yml file.

#     Returns:
#         Dict[str, str]: Dictionary mapping library names to their full version specification.
#     """
#     with yml_path.open() as f:
#         environment = yaml.safe_load(f)

#     libraries = {}
#     for dep in environment.get("dependencies", []):
#         if isinstance(
#             dep, dict
#         ):  # If the dependency is a dictionary (like pip packages), skip
#             continue
#         lib_name = re.split("=|<|>|!", dep)[0]  # Extract library name
#         libraries[lib_name] = dep

#     return libraries


# def extract_imports_from_directory(directory: str) -> set[str]:
#     """
#     Extracts all imports from Python files and Jupyter notebooks in a directory.

#     Args:
#         directory (str): Path to the directory to search.

#     Returns:
#         Set[str]: A set of unique imports from the directory.
#     """
#     all_imports = set()
#     for file_path in Path(directory).rglob("*"):
#         if file_path.suffix == ".ipynb":
#             all_imports.update(extract_imports_from_notebook(file_path))
#         elif file_path.suffix == ".py":
#             all_imports.update(extract_imports_from_python(file_path))
#     return all_imports


# def main(directory: str, yml_path: Path) -> None:
#     """
#     Main function to extract and match imports with dependencies from environment.yml.

#     Args:
#         directory (str): Directory to search for Python files and Jupyter notebooks.
#         yml_path (Path): Path to the environment.yml file.
#     """
#     all_imports = extract_imports_from_directory(directory)
#     environment_libraries = extract_libraries_from_environment_yml(yml_path)

#     # Filter dependencies based on imports
#     used_dependencies = {
#         k: v for k, v in environment_libraries.items() if k in all_imports
#     }

#     # Format the list of matches for YAML
#     formatted_imports = "\n  - ".join(used_dependencies.values())
#     output = f"dependencies:\n  - {formatted_imports}\n"
#     logging.info(output)


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(
#         description=(
#             "Extract imports from Python files and Jupyter notebooks in a directory and"
#             " filter based on environment.yml."
#         )
#     )
#     parser.add_argument(
#         "directory", help="Directory to search for Python files and Jupyter notebooks."
#     )
#     parser.add_argument(
#         "--yml",
#         default="environment.yml",
#         help=(
#             "Path to the environment.yml file (default is environment.yml in the"
#             " current directory)."
#         ),
#     )
#     args = parser.parse_args()
#     main(args.directory, Path(args.yml))

import argparse
import logging
import re
from pathlib import Path

import nbformat
import yaml

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def extract_imports_from_notebook(notebook_path: Path) -> set[str]:
    """
    Extracts import statements from a Jupyter notebook.
    """
    with notebook_path.open("r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)

    imports: set[str] = set()
    for cell in notebook.cells:
        if cell.cell_type == "code":
            code = cell.source
            matches = re.findall(
                r"^\s*(?:from\s+([\w\.]+)\s+)?import\s+([\w\.]+)", code, re.MULTILINE
            )
            for match in matches:
                imports.add(
                    match[0].split(".")[0] if match[0] else match[1].split(".")[0]
                )
    return imports


def extract_libraries_from_environment_yml(yml_path: Path) -> set[str]:
    """
    Extracts library names from an environment.yml file.
    """
    with yml_path.open("r", encoding="utf-8") as f:
        env = yaml.safe_load(f)

    libraries: set[str] = set()
    for dep in env.get("dependencies", []):
        if isinstance(dep, str):
            lib = dep.split("=")[0]
            libraries.add(lib)
    return libraries


def main(input_path: str, yml_path: str) -> None:
    """
    Main function to compare notebook imports with environment.yml dependencies.
    """
    input_path = Path(input_path)
    yml_path = Path(yml_path)

    if input_path.is_dir():
        notebooks = list(input_path.rglob("*.ipynb"))
    elif input_path.suffix == ".ipynb":
        notebooks = [input_path]
    else:
        logging.error("Input path must be a directory or a .ipynb file.")
        return

    all_imports: set[str] = set()
    for notebook in notebooks:
        notebook_imports = extract_imports_from_notebook(notebook)
        all_imports.update(notebook_imports)

    libraries = extract_libraries_from_environment_yml(yml_path)

    to_add = all_imports - libraries
    to_remove = libraries - all_imports

    if to_add:
        logging.info("Packages to add:")
        for pkg in sorted(to_add):
            logging.info(f"  - {pkg}")
    else:
        logging.info("No packages to add.")

    if to_remove:
        logging.info("\nPackages to remove:")
        for pkg in sorted(to_remove):
            logging.info(f"  - {pkg}")
    else:
        logging.info("No packages to remove.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compare notebook imports with environment.yml dependencies."
    )
    parser.add_argument(
        "input_path", help="Path to a notebook file or directory containing notebooks"
    )
    parser.add_argument("yml_path", help="Path to the environment.yml file")
    args = parser.parse_args()

    main(args.input_path, args.yml_path)
