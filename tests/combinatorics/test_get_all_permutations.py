import pytest
from rosalind.combinatorics import get_all_permutations


def test_get_all_permutations_positive_n():
    # Test with n=3
    result = get_all_permutations(3)
    expected = [
        (1, 2, 3),
        (1, 3, 2),
        (2, 1, 3),
        (2, 3, 1),
        (3, 1, 2),
        (3, 2, 1),
    ]
    assert result == expected


def test_get_all_permutations_one():
    # Test with n=1
    result = get_all_permutations(1)
    expected = [(1,)]
    assert result == expected


def test_get_all_permutations_zero():
    # Test with invalid input (n=0)
    with pytest.raises(ValueError):
        get_all_permutations(0)


def test_get_all_permutations_negative_n():
    # Test with invalid input (negative n)
    with pytest.raises(ValueError):
        get_all_permutations(-2)
