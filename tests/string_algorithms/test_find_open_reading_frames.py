from rosalind.string_algorithms import find_open_reading_frames


# Test cases
def test_find_open_reading_frames_single_orf():
    dna = "ATGAAATAG"
    expected_orfs = ["ATGAAATAG"]
    assert find_open_reading_frames(dna) == expected_orfs


def test_find_open_reading_frames_multiple_orfs():
    dna = "ATGAAATAGATGTTTTAG"
    expected_orfs = ["ATGAAATAG", "ATGTTTTAG"]
    assert find_open_reading_frames(dna) == expected_orfs


def test_find_open_reading_frames_no_orf():
    dna = "ATGAAAAAA"
    expected_orfs = []  # No stop codon
    assert find_open_reading_frames(dna) == expected_orfs


def test_find_open_reading_frames_with_nested_orfs():
    dna = "ATGAAATGAATAG"
    expected_orfs = ["ATGAAATGA"]  # Full ORF is considered
    assert find_open_reading_frames(dna) == expected_orfs


def test_find_open_reading_frames_empty_dna():
    dna = ""
    expected_orfs = []
    assert find_open_reading_frames(dna) == expected_orfs
