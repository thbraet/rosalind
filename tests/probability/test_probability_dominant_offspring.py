import pytest
from rosalind.probability import probability_dominant_offspring


def test_probability_dominant_offspring_basic():
    # Test with simple case of 1 organism of each type
    assert (
        pytest.approx(probability_dominant_offspring(1, 1, 1), 0.01) == 0.8333
    )


def test_probability_dominant_offspring_all_dominant():
    # Test case where all are homozygous dominant
    assert probability_dominant_offspring(10, 0, 0) == 1.0


def test_probability_dominant_offspring_all_recessive():
    # Test case where all are homozygous recessive
    assert probability_dominant_offspring(0, 0, 10) == 0.0


def test_probability_dominant_offspring_mixed_population():
    # Mixed population
    assert (
        pytest.approx(probability_dominant_offspring(4, 4, 4), 0.01) == 0.7651
    )


def test_probability_dominant_offspring_large_population():
    # Larger population test
    result = probability_dominant_offspring(100, 50, 25)
    assert 0.85 < result < 1.0


def test_rosalind_sample_input():
    result = probability_dominant_offspring(2, 2, 2)
    assert pytest.approx(result, 0.01) == 0.7833
