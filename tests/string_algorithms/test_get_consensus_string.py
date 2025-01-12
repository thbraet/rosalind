import pytest
from rosalind.string_algorithms import get_consensus_string


def test_get_consensus_string_basic():
    dna_list = ["ATCC", "AACC", "AATC", "ATGC"]
    result = get_consensus_string(dna_list)
    assert result == "AACC", f"Expected 'AACC', but got {result}"


def test_get_consensus_string_single_dna_string():
    dna_list = ["ACGT"]
    result = get_consensus_string(dna_list)
    assert result == "ACGT", f"Expected 'ACGT', but got {result}"


def test_get_consensus_string_empty_list():
    dna_list = []
    with pytest.raises(
        ValueError, match="The input list of DNA strings is empty."
    ):
        get_consensus_string(dna_list)


def test_get_consensus_string_invalid_input():
    dna_list = ["ACGT", "ACG"]
    with pytest.raises(
        ValueError, match="All DNA strings must be of the same length."
    ):
        get_consensus_string(dna_list)


def test_get_consensus_string_case_sensitivity():
    dna_list = ["acgt", "ACGT"]
    with pytest.raises(KeyError):
        get_consensus_string(dna_list)


def test_get_consensus_string_non_dna_characters():
    dna_list = ["ACGT", "ACBX"]
    with pytest.raises(KeyError):
        get_consensus_string(dna_list)


def test_rosalind_sample_problem():
    dna_list = [
        "ATCCAGCT",
        "GGGCAACT",
        "ATGGATCT",
        "AAGCAACC",
        "TTGGAACT",
        "ATGCCATT",
        "ATGGCACT",
    ]
    result = get_consensus_string(dna_list)
    assert result == "ATGCAACT"
