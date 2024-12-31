import pytest
from rosalind.string_algorithms import transcribe_dna_to_rna  # Replace with your actual module name

def test_transcribe_dna_to_rna_basic():
    # Test for a simple DNA sequence
    result = transcribe_dna_to_rna("ACGT")
    expected = "ACGU"
    assert result == expected

def test_transcribe_dna_with_multiple_ts():
    # Test for a DNA sequence with multiple 'T's
    result = transcribe_dna_to_rna("ATTGCAT")
    expected = "AUUGCAU"
    assert result == expected

def test_transcribe_dna_with_no_ts():
    # Test for a DNA sequence with no 'T's (no change)
    result = transcribe_dna_to_rna("ACG")
    expected = "ACG"
    assert result == expected

def test_transcribe_empty_dna():
    # Test for an empty DNA sequence
    result = transcribe_dna_to_rna("")
    expected = ""
    assert result == expected

def test_transcribe_dna_with_all_ts():
    # Test for a DNA sequence consisting of only 'T's
    result = transcribe_dna_to_rna("TTTT")
    expected = "UUUU"
    assert result == expected

def test_transcribe_dna_with_mixed_characters():
    # Test for a DNA sequence with a mix of 'A', 'C', 'G', and 'T'
    result = transcribe_dna_to_rna("AGCTAGCT")
    expected = "AGCUAGCU"
    assert result == expected

if __name__ == "__main__":
    pytest.main()
