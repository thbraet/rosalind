import pytest
from rosalind.string_algorithms import find_longest_common_substring  # Replace 'rosalind.string_algorithms' with your actual module if needed

@pytest.mark.parametrize(
    "dna_list, expected_result",
    [
        # Basic test cases
        (["ACGT", "ACGTA", "ACG"], ['ACG']),  # Common subsequence 'ACG'
        (["AGTAC", "GTACG", "TACG"], ['TAC']),  # Common subsequence 'TAC'
        (["ATCG", "TAGC", "CTGA"], ['A', 'C', 'G', 'T']),  # Multiple common subsequences
        (["AGCT", "GCTA", "TACG"], ['A', 'C', 'G', 'T']),  # Multiple common subsequences
        
        # Edge cases
        (["A", "A", "A"], ['A']),  # All single-character strings, common subsequence 'A'
        (["A", "G", "C"], []),  # Completely disjoint DNA strings
        (["ACGT", "TGCATG", "ACGTG"], ['A', 'C', 'G', 'T']),  # Multiple common substrings
        
        # Case with substrings at the edges
        (["ACGT", "CGTA", "TGAC"], ['A', 'C', 'G', 'T'])  # Common subsequences 'A', 'C', 'G', 'T'
    ]
)
def test_find_longest_common_substring(dna_list, expected_result):
    """
    Test the function `find_longest_common_substring` for different DNA string lists.
    
    This test checks basic functionality, edge cases, and cases with no common substrings,
    ensuring that the longest common subsequences are correctly identified and returned.

    Args:
        dna_list (List[str]): A list of DNA strings to test.
        expected_result (List[str]): The expected output list of longest common subsequences.
    """
    result = find_longest_common_substring(dna_list)
    
    # Ensure both lists contain the same elements (order doesn't matter)
    assert sorted(result) == sorted(expected_result), f"Expected {expected_result}, got {result}"
