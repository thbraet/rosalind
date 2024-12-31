import pytest
from rosalind.string_algorithms import get_gc_content  # Adjust the import according to your file structure

def test_get_gc_content_basic():
    # Test with a simple sequence
    assert get_gc_content("ACGT") == 0.5

def test_get_gc_content_all_cg():
    # Test with a sequence containing only C and G
    assert get_gc_content("CGCG") == 1.0

def test_get_gc_content_no_cg():
    # Test with a sequence containing no C or G
    assert get_gc_content("ATAT") == 0.0

def test_get_gc_content_empty():
    # Test with an empty string (edge case)
    assert get_gc_content("") == 0.0

def test_get_gc_content_single_cg():
    # Test with a sequence containing only one C or G
    assert get_gc_content("C") == 1.0
    assert get_gc_content("G") == 1.0

def test_get_gc_content_mixed():
    # Test with a sequence with mixed content
    assert get_gc_content("AACGTTGC") == 0.5 

def test_get_gc_content_all_other_chars():
    # Test with a sequence with no C or G but contains other characters
    assert get_gc_content("AAAAA") == 0.0
    assert get_gc_content("TTTTT") == 0.0

def test_get_gc_content_edge_case():
    # Test with a sequence of C and G, length 1
    assert get_gc_content("C") == 1.0
    assert get_gc_content("G") == 1.0
    # Test with a longer sequence
    assert get_gc_content("CGCGCGCGCG") == 1.0  # All C and G
