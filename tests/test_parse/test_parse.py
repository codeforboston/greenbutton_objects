"""
These tests parse all available Green Button XML files into Python objects
using the greenbutton_objects library. The parsed objects are then converted
to string representations. Finally, the string representations are compared
to saved expected outputs to verify parsing and representation generation
are working correctly.
"""

import itertools
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


def check_file(data_file: Path):
    """
    Compares the string form of a parsed XML to a saved text file.
    """
    atom_forest = parse.parse_feed(str(data_file))
    parsed_feed_representation = parse.parse_feed_representation(atom_forest)
    expected_result_file_name = (
        data_file.parent.parent.parent
        / "expected_results"
        / data_file.parent.name
        / data_file.with_suffix(".txt").name
    )
    with open(expected_result_file_name) as f:
        expected_lines = map(str.strip, f)
        result_lines = map(str.strip, parsed_feed_representation.splitlines())

        sentinel = object()
        for line_num, (expected_line, result_line) in enumerate(
            itertools.zip_longest(expected_lines, result_lines, fillvalue=sentinel), start=1
        ):
            if expected_line == "":
                continue
            if result_line == "":
                continue
            if expected_line is sentinel:
                assert False, f"Expected results ended before parsed results in file {data_file} {line_num}"
            elif result_line is sentinel:
                assert False, f"Parsed results ended before expected results in file {data_file} {line_num}"
            else:
                assert expected_line == result_line, f"Mismatch in file {data_file} at line {line_num}"


@pytest.mark.parametrize("data_file_name", map(str, (_ROOT_DIR / "data" / "electricity").iterdir()))
def test_parse_electricity_feed(data_file_name):
    """
    Verify that parsing an electricity XML files works as intended.
    """
    check_file(Path(data_file_name))


@pytest.mark.parametrize("data_file_name", map(str, (_ROOT_DIR / "data" / "natural_gas").iterdir()))
def test_parse_natural_gas_feed(data_file_name):
    """
    Verify that parsing a natural gas XML file works as intended.
    """
    check_file(Path(data_file_name))


@pytest.mark.parametrize("energy_source", ["electricity", "natural_gas"])
def test_quick(energy_source):
    """
    Very quick test that runs only one of of the files from each source
    """
    files = (_ROOT_DIR / "data" / energy_source).iterdir()
    data_file_name = next(files)
    check_file(data_file_name)


if __name__ == "__main__":
    save_expected_results("electricity")
    save_expected_results("natural_gas")
