import pytest
from rosalind.string_algorithms import split_rna_into_codons


def test_valid_rna_divisible_by_3():
    rna = "AUGCGAUAA"
    expected = ["AUG", "CGA", "UAA"]
    assert split_rna_into_codons(rna) == expected


def test_valid_rna_not_divisible_by_3():
    rna = "AUGCGAA"
    expected = ["AUG", "CGA", "A"]
    assert split_rna_into_codons(rna) == expected


def test_empty_rna():
    rna = ""
    expected = []
    assert split_rna_into_codons(rna) == expected


def test_short_rna():
    rna = "AU"
    expected = ["AU"]
    assert split_rna_into_codons(rna) == expected


def test_mixed_case_rna():
    rna = "aUgCgAuAa"
    expected = ["aUg", "CgA", "uAa"]
    assert split_rna_into_codons(rna) == expected
