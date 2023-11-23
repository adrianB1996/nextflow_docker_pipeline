import os

import pytest

import glob



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

def test_find_files():
    # Create temporary directory for testing
    temp_dir = os.path.join(os.getcwd(), "test_data")
    os.makedirs(temp_dir, exist_ok=True)

    # Create sample files
    bam_file = os.path.join(temp_dir, "test.bam")
    bed_file = os.path.join(temp_dir, "test.bed")
    with open(bam_file, "w"):
        pass
    with open(bed_file, "w"):
        pass

    # Find BAM and BED files
    bam_files = find_files(temp_dir, "*.bam")
    bed_files = find_files(temp_dir, "*.bed*")

    # Assert that the correct files were found
    assert bam_files == [bam_file]
    assert bed_files == [bed_file]
