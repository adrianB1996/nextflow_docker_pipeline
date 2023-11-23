from utility.find_files import find_files
from bed_bam_processes.process_of_bed_bam_files import iterate_bed_bam_pairs
import os
import pysam
import argparse


def main():
    """
    Main script for processing BAM and BED files.

    Args:
        input_folder (str): Path to the input folder containing BAM and BED files.
        output_folder (str): Path to the output folder for processed files.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process BAM and BED files.")
    parser.add_argument(
        "--input_folder",
        type=str,
        help="Path to the input folder containing BAM and BED files.",
        default="data/input",
    )
    parser.add_argument(
        "--output_folder",
        type=str,
        help="Path to the output folder for processed files.",
        default="data/processed",
    )
    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder

    # Main script
    # Step 1 get files in folder with certain expressions
    bam_files = find_files(input_folder, "*.bam")
    bed_files = find_files(input_folder, "*.bed*")
    sorted_bam_files = []

    # Step 2: Go over bam files sorting and indexing.
    for file in bam_files:
        pysam.sort(
            "-o", os.path.join(output_folder, f"sorted_{os.path.basename(file)}"), file
        )
        sorted_bam_files.append(
            os.path.join(output_folder, f"sorted_{os.path.basename(file)}")
        )
        pysam.index(
            "-o",
            os.path.join(output_folder, f"sorted_{os.path.basename(file)}.bai"),
            os.path.join(output_folder, f"sorted_{os.path.basename(file)}"),
        )

    # Process all bed-bam file pairs
    iterate_bed_bam_pairs(bed_files, sorted_bam_files, output_folder)


if __name__ == "__main__":
    main()
