import pytest
from rosalind.string_algorithms import find_glycosylation_motifs  # Replace with the actual import path

def test_valid_id_with_motifs():
    # Using a known UniProt ID with glycosylation motifs
    result = find_glycosylation_motifs("B5ZC00")
    assert result is not None, "Expected to find glycosylation motifs."
    assert "85" in result, "Expected motif at position 3."

def test_valid_id_without_motifs():
    # Using a known UniProt ID with no glycosylation motifs
    result = find_glycosylation_motifs("A2Z669")  # Replace with a real ID with no motifs
    assert result is None, "Expected None for a protein with no motifs."

def test_invalid_id():
    # Using an invalid UniProt ID
    result = find_glycosylation_motifs("INVALID_ID")
    assert result is None, "Expected None for an invalid UniProt ID."

def test_large_protein():
    # Using a UniProt ID for a very large protein sequence
    result = find_glycosylation_motifs("Q8WZ42")  # Replace with a real ID of a large protein
    assert result is not None, "Expected to find motifs in a large protein sequence."
    assert isinstance(result, str), "Result should be a string of positions."

def test_api_rate_limit():
    # Make multiple requests in a loop to check if rate limits are handled
    for _ in range(10):  # Replace 10 with a reasonable number for testing
        result = find_glycosylation_motifs("B5ZC00")
        assert result is not None, "Expected valid results even with repeated requests."
        
@pytest.mark.parametrize(
    "uniprot_id, expected_result",
    [
        ("P10643_CO7_HUMAN", "202 754"),         # Known ID with motifs at positions 202 and 754
        ("Q3Z2Z2", "49"),                       # Known ID with a motif at position 49
        ("P02725_GLP_PIG", "16 19 39"),         # Known ID with motifs at positions 16, 19, and 39
        ("P07359_GPBA_HUMAN", "37 175 362 398"),# Known ID with motifs at multiple positions
        ("P07585_PGS2_HUMAN", "211 262 303"),   # Known ID with motifs at positions 211, 262, and 303
        ("P01880_DTC_HUMAN", "225 316 367"),    # Known ID with motifs at positions 225, 316, and 367
        ("P72173", "87 284 383"),               # Known ID with motifs at positions 87, 284, and 383
        ("Q90304_C166_CARAU", "92 171 350 441 465"), # Known ID with multiple motifs
    ]
)
def test_find_glycosylation_motifs(uniprot_id, expected_result):
    result = find_glycosylation_motifs(uniprot_id)
    assert result == expected_result, f"Expected '{expected_result}' for '{uniprot_id}', but got '{result}'."
