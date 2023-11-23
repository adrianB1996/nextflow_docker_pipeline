import json
import os


def create_json_filename(filename):
    return f"{filename}.json"


def construct_output_path(output_dir, json_filename):
    return os.path.join(output_dir, json_filename)


def prepare_json_data(bed_file, bam_file, feature_counts):
    json_data = {
        "bed_file": bed_file,
        "bam_file": bam_file,
        "feature_counts": feature_counts,
    }
    return json_data


def write_json_data(output_path, json_data):
    with open(output_path, "w") as json_file:
        json.dump(json_data, json_file, indent=4)


def test_create_json_filename():
    assert create_json_filename("test.bed") == "test.bed.json"
    assert create_json_filename("example.bam") == "example.bam.json"


def test_construct_output_path():
    output_dir = "/test/test_data/output"
    json_filename = "test.bed.json"
    assert construct_output_path(output_dir, json_filename) == os.path.join(
        output_dir, json_filename
    )


def test_prepare_json_data():
    bed_file = "test.bed"
    bam_file = "example.bam"
    feature_counts = 100
    json_data = prepare_json_data(bed_file, bam_file, feature_counts)
    assert json_data == {
        "bed_file": bed_file,
        "bam_file": bam_file,
        "feature_counts": feature_counts,
    }
