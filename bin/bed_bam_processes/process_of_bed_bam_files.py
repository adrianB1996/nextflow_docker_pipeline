import gzip
import itertools
import json
import os

import pysam


def iterate_bed_bam_pairs(bed_files: list[str], bam_files: list[str], output_dir: str):
    """
    Processes pairs of BED and BAM files, calculating feature counts for each pair and writing the results to JSON files.

    Args:
        bed_files (list[str]): A list of BED file paths.
        bam_files (list[str]): A list of BAM file paths.
        output_dir (str): The directory where the JSON files should be saved.

    Returns:
        None
    """

    for bed_file, bam_file in itertools.product(bed_files, bam_files):
        # Process the bed and bam file pair and get the feature counts
        filename = f"{os.path.basename(bed_file)}_{os.path.basename(bam_file)}"

        feature_counts = process_bed_bam_pair(bed_file, bam_file, output_dir, filename)

        # Create the JSON filename by combining the bed and bam filenames
        json_filename = f"{filename}.json"

        # Construct the full output path
        output_path = os.path.join(output_dir, json_filename)

        # Prepare JSON data for the current bed-bam pair
        json_data = {
            "bed_file": bed_file,
            "bam_file": bam_file,
            "feature_counts": feature_counts,
        }

        # Write the combined JSON data to the specified output path
        with open(output_path, "w") as json_file:
            json.dump(json_data, json_file, indent=4)


def process_bed_bam_pair(
    bed_file: str, bam_file: str, output_folder: str, filename: str
):
    """
    Calculates feature counts for a given pair of BED and BAM files.

    Args:
        bed_file (str): The path to the BED file containing genomic features.
        bam_file (str): The path to the BAM file containing aligned reads.
        out_folder (str): The path to the output folder.
        filename (str): The filename for the fasta file.

    Returns:
        dict[str, int]: A dictionary mapping feature keys to their respective counts.
    """

    # Open the bed file and bam file
    with gzip.open(bed_file, "rt") as bed_handle, pysam.Samfile(
        bam_file, "rb"
    ) as bam_handle:
        # Create a dictionary to store feature counts
        feature_counts = {}

        # Iterate over the features in the bed file
        for line in bed_handle:
            # empty string for fasta file.
            reads = ""
            # Extract the feature information from the bed line
            chrom, start, end = line.strip().split("\t")

            # Create a key for the feature
            feature_key = f"{chrom}:{start}-{end}"

            # Initialize the count for the feature
            feature_counts.setdefault(feature_key, 0)

            # Iterate over the reads in the bam file that overlap the feature
            for read in bam_handle.fetch(chrom, int(start), int(end)):
                # Increment the count for the feature
                feature_counts[feature_key] += 1

                # Extract feature information.
                read_id = read.query_name
                read_seq = read.seq

                reads += f">{read_id}\n{read_seq}\n"

            # Step 3: Write the concatenated reads to a single FASTA file.
            output_file = os.path.join(output_folder, f"{filename}_{feature_key}.fasta")

            with open(output_file, "w") as outfile:
                outfile.write(reads)

    return feature_counts
