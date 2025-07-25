"""
This script checks markdown files for the presence of front matter.

Front matter is typically YAML metadata at the beginning of a markdown file,
enclosed between `---` delimiters.
"""

import os
import sys
import yaml


def scan_front_matter(file_path):
    """
    Scans a markdown file for front matter.

    Args:
        file_path (str): The path to the markdown file.

    Returns:
        dict or None: The parsed front matter as a dictionary, or None if no front matter is found.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print(f"Checking file: {file_path}")
        sys.stdout.flush()  # Ensure the output is flushed to the logs
        if content.startswith("---"):
            end = content.find("---", 3)
            if end != -1:
                front_matter = content[3:end].strip()
                return yaml.safe_load(front_matter)
    return None


def main():
    """
    Main function to check markdown files for missing front matter.

    It reads the list of files from the `PR_FILES` environment variable,
    scans each markdown file, and reports any files missing front matter.
    """
    pr_files = os.getenv("PR_FILES", "").split(",")
    pr_files = [file for file in pr_files if file]  # Filter out empty strings
    missing_front_matter = []
    for file in pr_files:
        if file.endswith(".md"):
            front_matter = scan_front_matter(file)
            if not front_matter:
                missing_front_matter.append(file)
    if missing_front_matter:
        result = f"{', '.join(missing_front_matter)} is missing front matter"
    else:
        result = "All markdown files have front matter."

    print(result)
    sys.stdout.flush()  # Ensure the output is flushed to the logs


if __name__ == "__main__":
    main()
