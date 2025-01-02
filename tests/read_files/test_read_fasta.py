import pytest
import pandas as pd
from rosalind.read_files import read_fasta  

# Test data for mocking
FASTA_CONTENT = """>seq1
ATGCATGC
>seq2
GATTACA
"""

INVALID_FASTA_CONTENT = """ATGCATGC
>seq2
GATTACA
"""

DUPLICATE_IDENTIFIER_FASTA_CONTENT = """>seq1
ATGCATGC
>seq1
GATTACA
"""

def test_read_fasta_valid(tmp_path):
    """Test that the function correctly parses a valid FASTA file."""
    print(tmp_path)
    
    fasta_file = tmp_path / "test.fasta"
    fasta_file.write_text(FASTA_CONTENT)

    expected_df = pd.DataFrame(
        {'Identifier': ['seq1', 'seq2'], 'Sequence': ['ATGCATGC', 'GATTACA']}
    )

    result_df = read_fasta(fasta_file)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_read_fasta_invalid_format(tmp_path):
    """Test that the function raises a ValueError for improperly formatted FASTA."""
    fasta_file = tmp_path / "test_invalid.fasta"
    fasta_file.write_text(INVALID_FASTA_CONTENT)

    with pytest.raises(ValueError, match="Sequence found before identifier."):
        read_fasta(fasta_file)

def test_read_fasta_duplicate_identifiers(tmp_path):
    """Test that the function raises a ValueError for duplicate identifiers."""
    fasta_file = tmp_path / "test_duplicate.fasta"
    fasta_file.write_text(DUPLICATE_IDENTIFIER_FASTA_CONTENT)

    with pytest.raises(ValueError, match="Duplicate identifier found: seq1"):
        read_fasta(fasta_file)

def test_read_fasta_file_not_found():
    """Test that the function raises a FileNotFoundError for missing files."""
    with pytest.raises(FileNotFoundError, match="FASTA file not found"):
        read_fasta("nonexistent.fasta")

def test_read_fasta_empty_file(tmp_path):
    """Test that the function raises a ValueError for an empty FASTA file."""
    fasta_file = tmp_path / "empty.fasta"
    fasta_file.write_text("")  # Write an empty file

    with pytest.raises(ValueError, match="The FASTA file is empty or improperly formatted."):
        read_fasta(fasta_file)
