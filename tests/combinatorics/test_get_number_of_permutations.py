import pytest
from rosalind.combinatorics import get_number_of_permutations


def test_get_number_of_permutations_positive_n():
    # Test with n=3
    assert get_number_of_permutations(3) == 6

def test_get_number_of_permutations_zero():
    # Test with n=0 (edge case)
    assert get_number_of_permutations(0) == 1

def test_get_number_of_permutations_one():
    # Test with n=1
    assert get_number_of_permutations(1) == 1

def test_get_number_of_permutations_negative_n():
    # Test with invalid input (negative n)
    with pytest.raises(ValueError):
        get_number_of_permutations(-3)