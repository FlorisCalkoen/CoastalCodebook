import argparse
import logging
import pathlib
import re

import nbformat
import yaml

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def extract_imports_from_notebook(notebook_path: pathlib.Path | str) -> set[str]:
    """
    Extracts import statements from a Jupyter notebook.
    """
    notebook_path = pathlib.Path(notebook_path)
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


def extract_libraries_from_environment_yml(yml_path: pathlib.Path | str) -> set[str]:
    """
    Extracts library names from an environment.yml file.
    """
    yml_path = pathlib.Path(yml_path)
    with yml_path.open("r", encoding="utf-8") as f:
        env = yaml.safe_load(f)

    libraries: set[str] = set()
    for dep in env.get("dependencies", []):
        if isinstance(dep, str):
            lib = dep.split("=")[0]
            libraries.add(lib)
    return libraries


def main(input_path: str | pathlib.Path, yml_path: str | pathlib.Path) -> None:
    """
    Main function to compare notebook imports with environment.yml dependencies.
    """
    input_path = pathlib.Path(input_path)
    yml_path = pathlib.Path(yml_path)

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
