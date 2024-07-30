"""
asdf
"""

import os
import pathlib
from pathlib import Path

import pytest
from greenbutton_objects import parse

_ROOT_DIR = pathlib.Path(__file__).parent


def _save_representation(test_xml_path: Path, test_output_path: Path) -> None:
    """
    Parse an XML feed, generate a representation, and save it to a text
    file.
    """
    parsed_feed = parse.parse_feed(test_xml_path)
    representation = parse.parse_feed_representation(parsed_feed)
    with open(test_output_path, "w") as f:
        f.write(representation)


def save_expected_results(energy_source):
    """
    Save the expected results of parsing each XML file of test data.

    Should be run only to update the expected results of parsing XML
    data or representing parsed data.
    """
    data_path = _ROOT_DIR / "data" / energy_source
    expected_results_path = _ROOT_DIR / "expected_results" / energy_source

    for data_file_name in os.listdir(data_path):
        result_file_name = data_file_name.strip("xml") + "txt"
        _save_representation(
            data_path / data_file_name,
            expected_results_path / result_file_name,
        )


@pytest.mark.parametrize("data_file_name", os.listdir(_ROOT_DIR / "data" / "electricity"))
def test_parse_electricity_feed(data_file_name):
    """
    Verify that parsing an electricity XML file works as intended.

    Compares the string form of a parsed XML to a saved text file.
    """
    data_path = _ROOT_DIR / "data" / "electricity"
    expected_results_path = _ROOT_DIR / "expected_results" / "electricity"

    parsed_feed = parse.parse_feed(data_path / data_file_name)
    parsed_feed_representation = parse.parse_feed_representation(parsed_feed)
    result_file_name = data_file_name.strip("xml") + "txt"
    expected_results_file = expected_results_path / result_file_name
    with open(expected_results_file) as f:
        for line_num, (expected_line, result_line) in enumerate(
            zip(f, parsed_feed_representation.splitlines()), start=1
        ):
            assert expected_line.strip("\n") == result_line.strip(
                "\n"
            ), f"Mismatch in file {data_file_name} at line {line_num}"


@pytest.mark.parametrize("data_file_name", os.listdir(_ROOT_DIR / "data" / "natural_gas"))
def test_parse_natural_gas_feed(data_file_name):
    """
    Verify that parsing a natural gas XML file works as intended.

    Compares the string form of a parsed XML to a saved text file.
    """
    data_path = _ROOT_DIR / "data" / "natural_gas"
    expected_results_path = _ROOT_DIR / "expected_results" / "natural_gas"

    parsed_feed = parse.parse_feed(data_path / data_file_name)
    parsed_feed_representation = parse.parse_feed_representation(parsed_feed)
    result_file_name = data_file_name.strip("xml") + "txt"
    expected_results_file = expected_results_path / result_file_name
    with open(expected_results_file) as f:
        for line_num, (expected_line, result_line) in enumerate(
            zip(f, parsed_feed_representation.splitlines()), start=1
        ):
            assert expected_line.strip("\n") == result_line.strip(
                "\n"
            ), f"Mismatch in file {data_file_name} at line {line_num}"


if __name__ == "__main__":
    save_expected_results("electricity")
    save_expected_results("natural_gas")
