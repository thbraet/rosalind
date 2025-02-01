from rosalind.string_algorithms import get_complementary_dna_strand


def test_complementary_strand_basic():
    # Test with a simple DNA sequence
    assert get_complementary_dna_strand("ATCG") == "CGAT"


def test_complementary_strand_reverse():
    # Test with a reverse sequence
    assert get_complementary_dna_strand("GATTACA") == "TGTAATC"


def test_complementary_strand_single_nucleotide():
    # Test with a single nucleotide
    assert get_complementary_dna_strand("A") == "T"
    assert get_complementary_dna_strand("T") == "A"
    assert get_complementary_dna_strand("C") == "G"
    assert get_complementary_dna_strand("G") == "C"


def test_complementary_strand_empty():
    # Test with an empty string (edge case)
    assert get_complementary_dna_strand("") == ""


def test_complementary_strand_all_nucleotides():
    # Test with a sequence containing all nucleotides
    assert get_complementary_dna_strand("ATCG") == "CGAT"
    assert get_complementary_dna_strand("TGCATG") == "CATGCA"


def test_complementary_strand_no_complementary():
    # Test with no complementary characters, should raise an error or return unchanged
    # For example, the function is designed to handle all valid nucleotide bases, so this may not apply.
    pass


def test_rosalind_sample_input():
    result = get_complementary_dna_strand("AAAACCCGGT")
    expected = "ACCGGGTTTT"
    assert result == expected
