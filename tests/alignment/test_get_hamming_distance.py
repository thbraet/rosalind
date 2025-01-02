import pytest

# Import the function
from rosalind.alignment import get_hamming_distance 

def test_hamming_distance_valid():
    # Test with strings of equal length and no differences
    assert get_hamming_distance("AGCT", "AGCT") == 0

    # Test with strings of equal length and some differences
    assert get_hamming_distance("AGCT", "ACGT") == 2

    # Test with completely different strings
    assert get_hamming_distance("AAAA", "TTTT") == 4

    # Test with a mix of case-sensitive characters
    assert get_hamming_distance("aGct", "AGCT") == 3

def test_hamming_distance_invalid_lengths():
    # Test with strings of different lengths
    with pytest.raises(ValueError, match="Strings must be of equal length."):
        get_hamming_distance("AGCT", "AGC")

def test_hamming_distance_empty_strings():
    # Test with two empty strings
    assert get_hamming_distance("", "") == 0

def test_hamming_distance_whitespace_strings():
    # Test with strings containing only whitespace
    assert get_hamming_distance("    ", "    ") == 0

def test_hamming_distance_special_characters():
    # Test with strings containing special characters
    assert get_hamming_distance("!@#$", "%^&*") == 4


