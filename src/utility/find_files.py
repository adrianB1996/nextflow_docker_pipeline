import glob
import os


def find_files(folder_path, expression):
    """
    Finds all files in the specified folder that match the given expression.

    Args:
        folder_path (str): The path to the folder to search.
        expression (str): A glob expression to match file names.

    Returns:
        list[str]: A list of file paths.
    """

    files = glob.glob(os.path.join(folder_path, expression))

    return files
