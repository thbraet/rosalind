import pytest
import pandas as pd
from rosalind.string_algorithms import find_reverse_palindromes


def test_valid_reverse_palindromes():
    """
    Test the function with valid input containing reverse palindromes.
    """
    dna_strand = "GAATTCGAATTC"
    df = find_reverse_palindromes(dna_strand, min_length=4, max_length=12)
    expected = pd.DataFrame(
        {
            "Position": [1, 1, 2, 2, 3, 4, 5, 7, 8],
            "Length": [6, 12, 4, 10, 8, 6, 4, 6, 4],
        }
    )
    pd.testing.assert_frame_equal(df, expected)


def test_invalid_min_length():
    """
    Test the function with an invalid minimum length.
    """
    dna_strand = "GAATTC"
    with pytest.raises(
        ValueError,
        match="min_length must be > 0 and max_length must be >= min_length.",
    ):
        find_reverse_palindromes(dna_strand, min_length=-1, max_length=10)


def test_invalid_characters():
    """
    Test the function with a sequence containing invalid characters.
    """
    dna_strand = "GAXTTC"
    with pytest.raises(
        KeyError, match="Invalid character\\(s\\) found in DNA sequence: {'X'}"
    ):
        find_reverse_palindromes(dna_strand, min_length=4, max_length=12)
