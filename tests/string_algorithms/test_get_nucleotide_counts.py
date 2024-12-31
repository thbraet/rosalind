import pytest
from rosalind.string_algorithms import get_nucleotide_counts

def test_dna_sequence():
    # Test for a DNA sequence
    result = get_nucleotide_counts("ACGTTAGC")
    expected = {'A': 2, 'C': 2, 'G': 2, 'T': 2, 'U': 0}
    assert result == expected

def test_rna_sequence():
    # Test for an RNA sequence
    result = get_nucleotide_counts("ACGUUAGC")
    expected = {'A': 2, 'C': 2, 'G': 2, 'U': 2, 'T': 0}
    assert result == expected

def test_empty_sequence():
    # Test for an empty sequence
    result = get_nucleotide_counts("")
    expected = {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'U': 0}
    assert result == expected

def test_no_u_in_dna():
    # Test a DNA sequence (should not have 'U')
    result = get_nucleotide_counts("ACGTTAGC")
    expected = {'A': 2, 'C': 2, 'G': 2, 'T': 2, 'U': 0}
    assert result == expected

def test_no_t_in_rna():
    # Test an RNA sequence (should not have 'T')
    result = get_nucleotide_counts("ACGUUAGC")
    expected = {'A': 2, 'C': 2, 'G': 2, 'T': 0, 'U': 2}
    assert result == expected

def test_single_nucleotide():
    # Test a sequence with only one type of nucleotide
    result = get_nucleotide_counts("AAAAA")
    expected = {'A': 5, 'C': 0, 'G': 0, 'T': 0, 'U': 0}
    assert result == expected

def test_different_order():
    # Test sequence with nucleotides in different order
    result = get_nucleotide_counts("GATCGA")
    expected = {'A': 2, 'C': 1, 'G': 2, 'T': 1, 'U': 0}
    assert result == expected

if __name__ == "__main__":
    pytest.main()
