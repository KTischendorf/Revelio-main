"""
This script checks the freshness of markdown files in a directory.

If a markdown file has not been updated in the past 6 months, a warning message
is added to the file to indicate that the information may be stale.
"""

import os
import subprocess
from datetime import datetime, timedelta

FRESHNESS = datetime.now() - timedelta(days=6 * 30)
WARNING_MESSAGE = """!!! danger "Trust but verify"
This document has not been updated in the past 6 months. The information contained within
may be stale. Proceed with healthy skepticism.\n"""


def get_markdown_files(directory):
    """
    Retrieves all markdown files in a directory.

    Args:
        directory (str): The directory to search.

    Returns:
        list: A list of markdown file paths.
    """
    markdown_files = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                markdown_files.append(os.path.join(root, filename))
    return markdown_files


def check_file(file_path):
    """
    Checks if a markdown file needs a freshness warning.

    Args:
        file_path (str): The path to the markdown file.
    """
    try:
        last_commit_date = subprocess.check_output(
            ["git", "log", "-1", "--format=%cd", "--", file_path], encoding="utf-8"
        ).strip()
        last_commit_time = datetime.strptime(
            last_commit_date, "%a %b %d %H:%M:%S %Y %z"
        ).replace(tzinfo=None)

        if last_commit_time < FRESHNESS:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            if WARNING_MESSAGE not in content:
                lines = content.split("\n")
                for i, line in enumerate(lines):
                    if line.startswith("#"):
                        lines.insert(i + 2, WARNING_MESSAGE)
                        break
                updated_content = "\n".join(lines)

                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(updated_content)
                print(f"Updated {file_path}")
            else:
                print(f"Warning message already present in {file_path}")
        else:
            print(f"{file_path} is fresh enough, no update needed.")
    except subprocess.CalledProcessError as error:
        print(f"Error checking file {file_path}: {error}")
    except FileNotFoundError as error:
        print(f"File not found: {file_path}. Error: {error}")
    except Exception as error:  # pylint: disable=broad-exception-caught
        print(f"Unexpected error processing file {file_path}: {error}")


def main():
    """
    Main function to check freshness of markdown files in the current directory.
    """
    markdown_files = get_markdown_files(".")
    for markdown_file in markdown_files:
        check_file(markdown_file)


if __name__ == "__main__":
    main()
