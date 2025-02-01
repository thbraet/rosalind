import pytest
from rosalind.probability import expected_dominant_offspring


def test_expected_dominant_offspring_example():
    # Test case 1: Example from docstring
    assert expected_dominant_offspring(10, 20, 15, 10, 25, 5) == 130.0


def test_expected_dominant_offspring_all_zero():
    # Test case 2: All zero couples
    assert expected_dominant_offspring(0, 0, 0, 0, 0, 0) == 0.0


def test_expected_dominant_offspring_all_AA_AA():
    # Test case 3: Only AA-AA couples
    assert expected_dominant_offspring(10, 0, 0, 0, 0, 0) == 20.0


def test_expected_dominant_offspring_all_Aa_Aa():
    # Test case 4: Only Aa-Aa couples
    assert expected_dominant_offspring(0, 0, 0, 10, 0, 0) == 15.0


def test_expected_dominant_offspring_all_aa_aa():
    # Test case 5: Only aa-aa couples
    assert expected_dominant_offspring(0, 0, 0, 0, 0, 10) == 0.0


def test_expected_dominant_offspring_mixed_couples():
    # Test case 6: Mixed couples
    assert expected_dominant_offspring(5, 5, 5, 5, 5, 5) == 42.5


def test_expected_dominant_offspring_custom_offspring():
    # Test case 7: Custom number of offspring per couple
    assert (
        expected_dominant_offspring(
            10, 20, 15, 10, 25, 5, nr_of_offspring_per_couple=3
        )
        == 195
    )


def test_expected_dominant_offspring_negative_genotype():
    # Test case 8: Negative genotype count (should raise ValueError)
    with pytest.raises(ValueError):
        expected_dominant_offspring(-1, 0, 0, 0, 0, 0)


def test_rosalind_sample_problem():
    assert expected_dominant_offspring(1, 0, 0, 1, 0, 1) == 3.5


def test_rosalind_iev():
    assert (
        expected_dominant_offspring(17402, 19651, 18780, 19472, 18229, 17774)
        == 159103.0
    )


def test_rosalind_iev2():
    assert (
        expected_dominant_offspring(18933, 19534, 17087, 19643, 19296, 19342)
        == 159868.5
    )
