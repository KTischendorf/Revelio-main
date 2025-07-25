"""
This script scans a directory for potential secret leaks.

It uses regular expressions and entropy calculations to identify potential secrets
like passwords, API keys, and tokens.
"""

import re
import os
import math
from concurrent.futures import ThreadPoolExecutor

PATTERNS = [
    re.compile(
        r"(?i)(password|passwd|token|api_key|secret|api_token|"
        r"api_secret|client_token|client_secret)\s*[:=\s]\s*([^\s]+)"
    ),
    re.compile(r"(?i)AWS_ACCESS_KEY_ID\s*=\s*([^\s]+)"),
    re.compile(r"(?i)GOOGLE_APPLICATION_CREDENTIALS\s*=\s*([^\s]+)"),
]


def is_hash(value):
    """
    Checks if a value is a hash.

    Args:
        value (str): The value to check.

    Returns:
        bool: True if the value is a hash, False otherwise.
    """
    return re.match(r"^[a-f0-9]{32,}$", value, re.IGNORECASE) is not None


def is_ignored(file_path, ignore_file=".secretignore"):
    """
    Checks if a file is in .secretignore.

    Args:
        file_path (str): The path to the file.
        ignore_file (str): The name of the ignore file.

    Returns:
        bool: True if the file is ignored, False otherwise.
    """
    if not os.path.exists(ignore_file):
        return False
    with open(ignore_file, "r", encoding="utf-8") as file:
        ignored_files = file.read().splitlines()
    return any(
        os.path.abspath(file_path).endswith(os.path.abspath(ignored_file))
        for ignored_file in ignored_files
    )


def is_text_file(file_path):
    """
    Checks if a file is ASCII or UTF-8 encoded.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file is a text file, False otherwise.
    """
    try:
        with open(file_path, "r", encoding="ascii") as file:
            file.read()
        return True
    except (UnicodeDecodeError, ValueError):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                file.read()
            return True
        except (UnicodeDecodeError, ValueError):
            return False


def calculate_entropy(data):
    """
    Calculates the entropy of a string.

    Args:
        data (str): The string to calculate entropy from.

    Returns:
        float: The entropy value.
    """
    if not data:
        return 0
    entropy = 0
    for char in set(data):
        p_x = float(data.count(char)) / len(data)
        if p_x > 0:
            entropy += -p_x * math.log(p_x, 2)
    return entropy


def scan_file(file_path, compiled_patterns):
    """
    Scans a file for secrets.

    Args:
        file_path (str): The path to the file.
        compiled_patterns (list): A list of compiled regex patterns.
    """
    if is_ignored(file_path) or not is_text_file(file_path):
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except UnicodeDecodeError:
        return

    for pattern in compiled_patterns:
        matches = pattern.findall(content)
        for match in matches:
            key, value = match
            if calculate_entropy(value) > 3.5 or is_hash(value):
                print(f"Potential leak found in {file_path}: {key}={value}")


def scan_directory(directory, compiled_patterns):
    """
    Scans a directory recursively for secrets.

    Args:
        directory (str): The path to the directory.
        compiled_patterns (list): A list of compiled regex patterns.
    """
    with ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                executor.submit(scan_file, file_path, compiled_patterns)
        executor.shutdown(wait=True)


if __name__ == "__main__":
    scan_directory(".", PATTERNS)
