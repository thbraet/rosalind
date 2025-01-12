import pytest
from rosalind.string_algorithms import find_substring_positions


def test_find_first_position():
    strand = "ACGTACGT"
    sub_strand = "CGT"
    result = find_substring_positions(strand, sub_strand, "first")
    assert result == 2


def test_find_last_position():
    strand = "ACGTACGT"
    sub_strand = "CGT"
    result = find_substring_positions(strand, sub_strand, "last")
    assert result == 6


def test_find_all_positions():
    strand = "AAAAAA"
    sub_strand = "AA"
    result = find_substring_positions(strand, sub_strand, "all")
    assert result == [1, 2, 3, 4, 5]


def test_find_no_position():
    strand = "ACGTACGT"
    sub_strand = "GGG"
    result = find_substring_positions(strand, sub_strand, "first")
    assert result == -1


def test_find_first_position_empty_strand():
    strand = ""
    sub_strand = "CGT"
    result = find_substring_positions(strand, sub_strand, "first")
    assert result == -1


def test_find_first_position_empty_sub_strand():
    strand = "ACGTACGT"
    sub_strand = ""
    result = find_substring_positions(strand, sub_strand, "first")
    assert result == -1


def test_find_all_positions_multiple_occurrences():
    strand = "ACGACGACG"
    sub_strand = "CG"
    result = find_substring_positions(strand, sub_strand, "all")
    assert result == [2, 5, 8]


def test_find_last_position_multiple_occurrences():
    strand = "ACGACGACG"
    sub_strand = "CG"
    result = find_substring_positions(strand, sub_strand, "last")
    assert result == 8


def test_rosalind_sample_input():
    strand = "GATATATGCATATACTT"
    sub_strand = "ATAT"
    result = find_substring_positions(strand, sub_strand, "all")
    expected = [2, 4, 10]
    assert result == expected
