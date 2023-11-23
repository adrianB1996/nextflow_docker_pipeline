import argparse

import pytest


def test_parse_arguments():
    # Construct mock arguments
    mock_args = [
        "--input_folder",
        "test_input_folder",
        "--output_folder",
        "test_output_folder",
    ]

    # Parse mock arguments using argparse
    parser = argparse.ArgumentParser(description="Process BAM and BED files.")
    parser.add_argument("--input_folder", type=str)
    parser.add_argument("--output_folder", type=str)

    parsed_args = parser.parse_args(mock_args)

    # Validate that parsed arguments match mock arguments
    assert parsed_args.input_folder == "test_input_folder"
    assert parsed_args.output_folder == "test_output_folder"


if __name__ == "__main__":
    pytest.main()
