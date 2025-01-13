import requests
from rosalind.read_files import read_codon_dict
import re
from typing import List
import pandas as pd


def get_nucleotide_counts(sequence: str) -> dict[str, int]:
    """
    Count the frequency of each nucleotide (A, C, G, T, U) in a given DNA or RNA sequence.

    Args:
        strand (str): A string representing the DNA or RNA sequence, consisting of the characters 'A', 'C', 'G', 'T' (DNA) or 'A', 'C', 'G', 'U' (RNA).

    Returns:
        dict[str, int]: A dictionary where the keys are the nucleotides ('A', 'C', 'G', 'T', 'U') and the values are their respective counts in the DNA or RNA sequence.

    Example:
        >>> get_nucleotide_counts("ACGTTAGC")
        {'A': 2, 'C': 2, 'G': 2, 'T': 2, 'U': 0}
        >>> get_nucleotide_counts("ACGUUAGC")
        {'A': 2, 'C': 2, 'G': 2, 'U': 2, 'T': 0}
    """
    # Include 'U' for RNA and 'T' for DNA
    freq_dict = {
        nucleotide: sequence.count(nucleotide) for nucleotide in "ACGTU"
    }
    return freq_dict


def transcribe_dna_to_rna(dna_sequence: str) -> str:
    """
    Transcribe a DNA sequence to an RNA sequence by replacing all occurrences of 'T' with 'U'.

    Args:
        dna_sequence (str): A string representing the DNA sequence, consisting of the characters 'A', 'C', 'G', and 'T'.

    Returns:
        str: A string representing the RNA sequence, where all occurrences of 'eT' in the DNA sequence
             are replaced with 'U'.

    Example:
        >>> transcribe_dna_to_rna("ACGT")
        'ACGU'

        >>> transcribe_dna_to_rna("ATTGCAT")
        'AUUGCAU'
    """
    return dna_sequence.replace("T", "U")[::-1]


def get_complementary_dna_strand(dna_sequence: str) -> str:
    """
    Generate the complementary strand of a given DNA sequence by replacing each nucleotide
    with its complementary base and reversing the sequence.

    The function follows these base-pairing rules:
    - A (Adenine) is complemented by T (Thymine)
    - T (Thymine) is complemented by A (Adenine)
    - C (Cytosine) is complemented by G (Guanine)
    - G (Guanine) is complemented by C (Cytosine)

    Args:
        dna_sequence (str): A string representing the DNA sequence, consisting of the characters 'A', 'T', 'C', and 'G'.

    Returns:
        str: A string representing the complementary DNA strand, where each nucleotide is replaced by its complement,
             and the sequence is reversed.

    Example:
        >>> get_complementary_dna_strand("ATCG")
        'CGAT'

        >>> get_complementary_dna_strand("GATTACA")
        'TGAATCT'
    """
    # Define the translation table for nucleotide replacement
    translation_table = str.maketrans("ATCG", "TAGC")
    # Reverse the DNA sequence and translate it using the table
    return dna_sequence[::-1].translate(translation_table)


def get_gc_content(dna_sequence: str) -> float:
    """
    Calculate the relative amount of 'C' and 'G' characters compared to the total length of the DNA sequence.

    Args:
        dna_sequence (str): A string representing the DNA sequence, consisting of the characters 'A', 'C', 'G', and 'T'.

    Returns:
        float: The relative amount of 'C' and 'G' characters in the DNA sequence, expressed as a decimal
               between 0 and 1. A value of 0 means no 'C' or 'G', while 1 means all characters are 'C' or 'G'.

    Example:
        >>> get_gc_content("ACGT")
        0.5

        >>> get_gc_content("CGCG")
        1.0

        >>> get_gc_content("ATAT")
        0.0
    """
    # Count the occurrences of 'C' and 'G' in the DNA sequence
    cg_count = dna_sequence.count("C") + dna_sequence.count("G")

    # Calculate the relative amount (CG count divided by total length)
    return cg_count / len(dna_sequence) if dna_sequence else 0.0


def find_substring_positions(
    strand: str, sub_strand: str, position_type: str = "all"
) -> int | list[int]:
    """
    Find all the starting positions of a substring within a DNA string.

    Args:
        strand (str): The DNA sequence.
        sub_strand (str): The substring to search for within the DNA sequence.
        position_type (str, optional): A string that specifies which positions to return. Can be "first", "last", or "all". Default is "last".

    Returns:
        int or list[int]: An integer for the "first" or "last" position, or a list of integers for "all" positions.

    Example:
        >>> find_substring_positions("ACGTACGT", "CGT", "first")
        2

        >>> find_substring_positions("AAAAAA", "AA", "all")
        [1, 2, 3, 4, 5]

        >>> find_substring_positions("AGCTAGC", "TC", "last")
        4
    """
    if sub_strand == "":
        return -1

    positions = []
    for i in range(len(strand) - len(sub_strand) + 1):
        if strand[i : i + len(sub_strand)] == sub_strand:
            positions.append(i + 1)  # 1-based index

    if position_type == "first":
        # Return the first occurrence
        return positions[0] if positions else -1  # Return -1 if no match

    elif position_type == "last":
        # Return the last occurrence
        return positions[-1] if positions else -1  # Return -1 if no match

    # Default behavior: return all positions
    return positions if positions else []


def split_rna_into_codons(rna: str) -> list[str]:
    """
    Splits an RNA sequence into codons.

    A codon is a sequence of three RNA nucleotides. This function takes a string representing an RNA sequence
    and splits it into a list of codons, where each codon is a substring of three nucleotides.

    Args:
        rna (str): The RNA sequence to split. It should consist of a valid RNA nucleotide sequence (A, U, G, C).

    Returns:
        list[str]: A list of codons, each represented as a string of three nucleotides.
    """
    return [rna[i : i + 3] for i in range(0, len(rna), 3)]


def translate_rna_to_protein(rna: str) -> str:
    """
    Translates an RNA sequence into a protein string.

    This function takes an RNA sequence, splits it into codons, and translates each codon into its corresponding
    amino acid based on a codon dictionary. Translation stops if a "Stop" codon is encountered.

    Args:
        rna (str): The RNA sequence to translate. It should consist of a valid RNA nucleotide sequence (A, U, G, C).

    Returns:
        str: The protein string resulting from translating the RNA sequence. Stop codons are not included in the output.
    """
    codon_dict = read_codon_dict()

    protein_string = ""

    codons = split_rna_into_codons(rna)

    for c in codons:
        if len(c) < 3:
            break
        protein = codon_dict[c]
        if protein == "Stop":
            break
        protein_string += protein

    return protein_string


def get_profile_matrix(dna_list: List[str]) -> pd.DataFrame:
    """
    Generate a profile matrix from a list of DNA strings.

    The profile matrix represents the frequency of each nucleotide (A, C, G, T)
    at each position in the DNA strings. The function assumes all DNA strings
    in the list are of equal length.

    Parameters:
        dna_list (List[str]): A list of DNA strings, where each string represents
                              a sequence of nucleotides (e.g., "ACGT").

    Returns:
        pd.DataFrame: A pandas DataFrame with rows for nucleotides ('A', 'C', 'G', 'T')
                      and columns corresponding to the positions in the DNA strings.
                      The values represent the count of each nucleotide at each position.

    Example:
        >>> dna_list = ["ACGT", "ACGT", "AGGT"]
        >>> get_profile_matrix(dna_list)
           0  1  2  3
        A  3  0  0  0
        C  0  3  0  0
        G  0  0  3  2
        T  0  0  0  1

    Raises:
        ValueError: If the input DNA strings have different lengths.
    """
    # Validate input
    if not dna_list:
        raise ValueError("The input list of DNA strings is empty.")

    if len(set(len(seq) for seq in dna_list)) != 1:
        raise ValueError("All DNA strings must be of the same length.")

    valid_nucleotides = {"A", "C", "G", "T"}
    if not all(set(dna).issubset(valid_nucleotides) for dna in dna_list):
        raise KeyError(
            "DNA strings contain invalid characters. Only 'A', 'C', 'G', 'T' are allowed."
        )

    # Convert DNA strings to a DataFrame
    dna_strings_to_df = pd.DataFrame([list(seq) for seq in dna_list])

    # Create profile matrix
    profile_matrix = pd.DataFrame(
        (
            (dna_strings_to_df == "A").sum().values,
            (dna_strings_to_df == "C").sum().values,
            (dna_strings_to_df == "G").sum().values,
            (dna_strings_to_df == "T").sum().values,
        ),
        index=["A", "C", "G", "T"],
    )

    return profile_matrix


def get_consensus_string(dna_list: List[str]) -> str:
    """
    Generate the consensus string from a list of DNA strings.

    The consensus string is derived by calculating the most frequent nucleotide
    at each position across all DNA strings in the list. This is determined
    using the profile matrix.

    Parameters:
        dna_list (List[str]): A list of DNA strings, where all strings are of the same length.

    Returns:
        str: The consensus string, which represents the most frequent nucleotide
             at each position across the DNA strings.

    Raises:
        ValueError: If the input list is empty or DNA strings are not of equal length.
        KeyError: If the DNA strings contain invalid characters.
    """

    profile_matrix = get_profile_matrix(dna_list)
    consensus_string = "".join(profile_matrix.idxmax().values)
    return consensus_string


def find_glycosylation_motifs(uniprot_id: str) -> list[int] | None:
    """
    Find N-glycosylation motifs in the protein sequence for a given UniProt ID.

    This function fetches the FASTA sequence of a protein from the UniProt database using the given UniProt ID,
    identifies N-glycosylation motifs (using the regex pattern `N[^P][ST][^P]`), and returns their start positions
    in the sequence.

    Args:
        uniprot_id (str): The UniProt ID of the protein (e.g., "P12345_HUMAN").

    Returns:
        list[int] | None: A list of 1-based start positions of the motifs, or None if:
            - The UniProt ID is invalid.
            - No glycosylation motifs are found.
            - The API request fails.

    Raises:
        requests.exceptions.RequestException: If there is an error while making the API request.

    Examples:
        >>> find_glycosylation_motifs("P12345_HUMAN")
        [3, 17, 29]

        >>> find_glycosylation_motifs("INVALID_ID")
        None
    """
    # Extract the UniProt accession number from the input
    id = uniprot_id.split("_")[0]

    # Fetch the FASTA data from the UniProt REST API
    url = f"https://rest.uniprot.org/uniprotkb/{id}.fasta"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data for {uniprot_id}. Error: {e}")
        return None

    # Parse the FASTA response
    fasta_data = response.text
    lines = fasta_data.splitlines()
    sequence = "".join(
        line.strip()
        for line in lines
        if not line.startswith(">") and line.isalpha()
    )

    # Regular expression for the N-glycosylation motif
    pattern = r"N(?=[^P][ST][^P])"  # Lookahead to allow overlapping matches

    # Find all overlapping matches and their start indices
    start_positions = [
        match.start() + 1 for match in re.finditer(pattern, sequence)
    ]  # Convert to 1-based indexing

    # Return the list of positions, or None if no matches
    return start_positions if start_positions else None


def find_common_substrings(s1: str, s2: str) -> List[str]:
    """
    Find all common substrings between two given strings.

    This function iterates through all substrings of the first string (`s1`)
    and checks if they exist in the second string (`s2`). It returns a list
    of unique common substrings.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.

    Returns:
        List[str]: A list of unique common substrings shared by `s1` and `s2`.

    Examples:
        >>> find_common_substring("hello", "yellow")
        ['e', 'ell', 'o', 'l', 'lo']

        >>> find_common_substring("abc", "def")
        []
    """
    common_substrings = []

    for i in range(len(s1)):
        for j in range(i, len(s1)):
            substring = s1[i : j + 1]
            if substring in s2:
                common_substrings.append(substring)

    # Remove duplicates by converting the list to a set and back to a list
    return list(set(common_substrings))


def find_longest_common_substring(dna_list: List[str]) -> List[str]:
    """
    Find the longest common subsequence (LCS) among a list of DNA strings.

    This function identifies the longest subsequence that is common across all DNA strands in the input list.
    The DNA strings are compared pair by pair, starting with the shortest two, and their common substrings are
    filtered through the remaining DNA strands.

    Args:
        dna_list (List[str]): A list of DNA strings, where each string represents a sequence of nucleotides.

    Returns:
        List[str]: A list of the longest common subsequences found among the input DNA strings, sorted alphabetically.

    Examples:
        >>> find_lcs(["ACGT", "ACGTA", "ACG"])
        ['ACG']

        >>> find_lcs(["AGTAC", "GTACG", "TACG"])
        ['ACG']

        >>> find_lcs(["ATCG", "TAGC", "CTGA"])
        ['A', 'C', 'G']

        >>> find_lcs(["AGCT", "GCTA", "TACG"])
        []
    """
    # Sort DNA strands by length (shortest first)
    dna_list_sorted = sorted(dna_list, key=len, reverse=False)

    # Find common substrings between the first two DNA strands
    substring_list = find_common_substrings(
        dna_list_sorted[0], dna_list_sorted[1]
    )

    # Filter common substrings across all DNA strands
    for dna_strand in dna_list_sorted:
        substring_list = [x for x in substring_list if x in dna_strand]

    if len(substring_list) == 0:
        return []

    # Find the maximum length of the common substrings
    max_length = max(len(s) for s in substring_list)

    print(substring_list)

    # Filter substrings that have the maximum length
    longest_strings = [s for s in substring_list if len(s) == max_length]

    return sorted(longest_strings)


def find_reverse_palindromes(
    dna_strand: str, min_length: int = 4, max_length: int = 12
) -> pd.DataFrame:
    """
    Locate positions and lengths of palindromic sequences (reverse palindromes)
    in a given DNA strand.

    A reverse palindrome is identified when a substring of the DNA strand
    is equal to its reverse complement. The search is performed for substrings
    between the specified minimum and maximum lengths.

    Args:
        dna_strand (str): A string representing the DNA strand.
        min_length (int): Minimum length of the palindromic substring to consider.
        max_length (int): Maximum length of the palindromic substring to consider.

    Raises:
        ValueError: If min_length or max_length are invalid.
        KeyError: If invalid characters are present in the DNA strand.

    Returns:
        pd.DataFrame: A DataFrame with columns 'Position' (1-based index) and 'Length'.
    """
    # Validate min_length and max_length
    if not (min_length > 0 and max_length >= min_length):
        raise ValueError(
            "min_length must be > 0 and max_length must be >= min_length."
        )

    # Validate that the sequence contains only valid nucleotides
    valid_nucleotides = set("ATCG")
    if not set(dna_strand).issubset(valid_nucleotides):
        raise KeyError(
            f"Invalid character(s) found in DNA sequence: {set(dna_strand) - valid_nucleotides}"
        )

    results: List[dict] = []

    # Locate reverse palindromes
    for i in range(len(dna_strand)):
        for j in range(
            i + min_length, min(i + max_length + 1, len(dna_strand) + 1)
        ):
            substring = dna_strand[i:j]
            if substring == get_complementary_dna_strand(substring):
                results.append({"Position": i + 1, "Length": len(substring)})

    return pd.DataFrame(results)
