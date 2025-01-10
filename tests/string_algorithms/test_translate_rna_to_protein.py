import pytest
from rosalind.string_algorithms import translate_rna_to_protein

def test_valid_rna_with_stop():
    rna = "AUGUUUUAA"
    expected = "MF"  # Methionine (AUG), Phenylalanine (UUU), stops at UAA
    assert translate_rna_to_protein(rna) == expected

def test_valid_rna_without_stop():
    rna = "AUGUUUGCUUGG"
    expected = "MFAW"  # Methionine (AUG), Phenylalanine (UUU), Alanine (GCU), Tryptophan (UGG)
    assert translate_rna_to_protein(rna) == expected

def test_empty_rna():
    rna = ""
    expected = ""  # No codons to translate
    assert translate_rna_to_protein(rna) == expected

def test_partial_codons():
    rna = "AUGUUUCG"
    expected = "MF"  # Last partial codon "CG" is ignored
    assert translate_rna_to_protein(rna) == expected

def test_rna_with_multiple_stop_codons():
    rna = "AUGUUUUAAUAGUGA"
    expected = "MF"  # Translation stops at the first stop codon (UAA)
    assert translate_rna_to_protein(rna) == expected

def test_rna_with_only_stop_codons():
    rna = "UAAUAGUGA"
    expected = ""  # No amino acids translated before stop codons
    assert translate_rna_to_protein(rna) == expected
