import pytest
import pandas as pd
from rosalind.string_algorithms import (
    get_profile_matrix,
)  # Replace with your actual module name


def test_get_profile_matrix_basic():
    dna_list = ["ACGT", "ACGT", "AGGT"]
    result = get_profile_matrix(dna_list)

    # Expected profile matrix
    expected_data = {
        0: [3, 0, 0, 0],  # A, C, G, T counts for column 0
        1: [0, 2, 1, 0],  # A, C, G, T counts for column 1
        2: [0, 0, 3, 0],  # A, C, G, T counts for column 2
        3: [0, 0, 0, 3],  # A, C, G, T counts for column 3
    }
    expected = pd.DataFrame(expected_data, index=["A", "C", "G", "T"])

    pd.testing.assert_frame_equal(result, expected)


def test_get_profile_matrix_different_input():
    dna_list = ["AAAA", "CCCC", "GGGG", "TTTT"]
    result = get_profile_matrix(dna_list)

    # Expected profile matrix
    expected_data = {
        0: [1, 1, 1, 1],  # A, C, G, T counts for column 0
        1: [1, 1, 1, 1],  # A, C, G, T counts for column 1
        2: [1, 1, 1, 1],  # A, C, G, T counts for column 2
        3: [1, 1, 1, 1],  # A, C, G, T counts for column 3
    }
    expected = pd.DataFrame(expected_data, index=["A", "C", "G", "T"])

    pd.testing.assert_frame_equal(result, expected)


def test_get_profile_matrix_single_string():
    dna_list = ["ACGT"]
    result = get_profile_matrix(dna_list)

    # Expected profile matrix
    expected_data = {
        0: [1, 0, 0, 0],  # A, C, G, T counts for column 0
        1: [0, 1, 0, 0],  # A, C, G, T counts for column 1
        2: [0, 0, 1, 0],  # A, C, G, T counts for column 2
        3: [0, 0, 0, 1],  # A, C, G, T counts for column 3
    }
    expected = pd.DataFrame(expected_data, index=["A", "C", "G", "T"])

    pd.testing.assert_frame_equal(result, expected)


def test_get_profile_matrix_invalid_input():
    dna_list = ["ACGT", "ACG"]
    with pytest.raises(
        ValueError, match="All DNA strings must be of the same length."
    ):
        get_profile_matrix(dna_list)


def test_get_profile_matrix_empty_input():
    dna_list = []
    with pytest.raises(
        ValueError, match="The input list of DNA strings is empty."
    ):
        get_profile_matrix(dna_list)


def test_get_profile_matrix_case_sensitivity():
    dna_list = ["acgt", "ACGT"]
    with pytest.raises(KeyError):
        get_profile_matrix(dna_list)


def test_get_profile_matrix_non_dna_characters():
    dna_list = ["ACGT", "ACBX"]
    with pytest.raises(KeyError):
        get_profile_matrix(dna_list)
