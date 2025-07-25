import os
import re


def check_snake_case(path):
    """
    Checks if file and directory names in the given path follow snake_case naming conventions.

    Args:
        path (str): The directory path to check.

    Returns:
        tuple: A list of invalid names and a dictionary of suggested renames.
    """
    pattern = re.compile(r"^[a-zA-Z0-9_.-]+$")
    invalid_names = []
    suggestions = {}
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for name in dirs + files:
            if not pattern.match(name) or " " in name or re.search(r"[^\w.-]", name):
                full_path = os.path.join(root, name)
                invalid_names.append(full_path)
                dir_path, file_name = os.path.split(full_path)
                suggested_name = file_name.replace(" ", "_").replace("&", "and_")
                suggested_name = re.sub(r"[^\w.-]", "", suggested_name)
                suggested_name = re.sub(r"^_+|_+$", "", suggested_name)
                suggested_name = re.sub(r"__+", "_", suggested_name)
                name, ext = os.path.splitext(suggested_name)
                suggested_name = f"{name.rstrip('_')}{ext}"
                suggested_full_path = os.path.join(dir_path, suggested_name)
                suggestions[full_path] = suggested_full_path
    return invalid_names, suggestions


def escape_special_characters(path):
    """
    Escapes special characters in a file path.

    Args:
        path (str): The file path to escape.

    Returns:
        str: The escaped file path.
    """
    special_chars = r"([$!#()&*?<>|{}[\]\\\\])"
    return re.sub(special_chars, r"\\\1", path)


if __name__ == "__main__":
    INVALID_NAMES, SUGGESTIONS = check_snake_case(".")
    if INVALID_NAMES:
        print("\nInvalid names found:")
        print("--------------------")
        for name in INVALID_NAMES:
            print(name)
        print("\nSuggested renames:")
        print("------------------")
        for original, suggested in SUGGESTIONS.items():
            print(f"{original} -> {suggested}")
        print("\nSample commands:")
        print("----------------")
        print("git pull --rebase")
        for original, suggested in SUGGESTIONS.items():
            escaped_original = escape_special_characters(original)
            escaped_suggested = escape_special_characters(suggested)
            print(f"\nmv {escaped_original} {escaped_suggested}")
        print("\ngit add .")
        print('\ngit commit -m "Updating file names"')
        print("\ngit push")
        exit(1)
    print("All names are valid.")
    exit(0)
